import yfinance as yf
import pandas_datareader as web
import numpy as np
import pandas as pd

#create class to acces data easy
class data:
    def __init__(self, input_stock, input_start_date, input_end_date):
        #define the input variables for the price_data
        self.stock = input_stock
        self.start = input_start_date
        self.end = input_end_date
        #select the right stock from the class input
        price_data = yf.Ticker(input_stock)
        #acces the data about the stock
        price_data = web.DataReader(input_stock, data_source = "yahoo", start = input_start_date, end= input_end_date)
        #calculate the change in price using the python diff function
        price_data["Change In Price"] = price_data["Close"].diff()

        n = 14
        #copy the data
        low_14 = price_data[['Low']].copy()
        #copy data
        high_14 = price_data[['High']].copy()
        #find the 14 day lowest value
        low14 = low_14['Low'].transform(lambda x: x.rolling(window = n).min())
        #find the highest 14 day value
        high14 = high_14['High'].transform(lambda x: x.rolling(window = n).max())
        #append the new variables to data set
        price_data['Low14'] = low14
        price_data['High14'] = high14

        #RSI
        n = 14

        up_df, down_df = price_data[['Change In Price']].copy(), price_data[['Change In Price']].copy()
        #for up days if the change is smaller than 0 set it to 0
        #for down days if the change is greater than 0 set it to 0
        up_df.loc['Change in Price'] = up_df.loc[(up_df['Change In Price'] < 0), 'Change In Price'] = 0
        down_df.loc['Change In Price'] = down_df.loc[(down_df['Change In Price'] > 0), 'Change In Price'] = 0

        #change the variable to an absolute variable
        down_df['Change In Price'] = down_df['Change In Price'].abs()
        #calculate the EWMA (Exponential Wheigtet Moving Average), older values are given less weight than newer values
        ewma_up = up_df['Change In Price'].transform(lambda x: x.ewm(span = n).mean())
        ewma_down = down_df['Change In Price'].transform(lambda x: x.ewm(span = n).mean())
        #calculate the relative strength "RS"
        relative_strength = ewma_up/ewma_down
        #calculate the relative strength index "RSI"
        relative_strength_index = 100.0 -(100.0 / (1.0+(relative_strength)))
        #add the new lines to the dataframe
        price_data['Change In Price'] = down_df['Change In Price']
        price_data['Change In Price'] = up_df['Change In Price']
        price_data['RSI'] = relative_strength_index


        #stochiastic oscilator
        A = price_data["Close"]-price_data["Low14"]
        B = price_data["High14"]-price_data["Low14"]

        K_percent = A/B*100

        price_data["K%"] = K_percent

        close_groups = price_data["Close"].transform(lambda x : np.sign(x.diff()))

        price_data["Prediction"] = close_groups
        price_data.loc[price_data["Prediction"] == 0.0] = 1.0
        

        price_data = price_data.dropna()
        
        self.price_data = price_data

        self.price_data = price_data