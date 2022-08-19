import yfinance as yf
import pandas as pd

stock = input("Enter stock: ")
start_date = input("Enter start date: ")
end_date = input("Enter end date: ")
candle_time = input("Enter candle time: ")

class data:
    def __init__(self, stock, start_date, end_date, candle_time):

        self.stock = stock
        self.start_date = start_date
        self.end_date = end_date
        self.intervall = candle_time
        
        price_data = yf.download(stock, start_date=start_date, end=end_date, candle_time = candle_time)
        
        #calculate the change in price using the python diff function
        price_data["Change In Price"] = price_data["Close"].diff()

        #calculate low14 / high 14
        n = 14
        #copy low / high column for calculation
        low14 = price_data["Low"].copy()
        high14 = price_data["High"].copy()
        #calculating low14 / high14
        low14 = price_data["Low"].transform(lambda x: x.rolling(window = n).min())
        high14 = price_data["High"].transform(lambda x: x.rolling(window = n).max())
        #assign low14 / high14 to dataframe
        price_data["Low14"] = low14
        price_data["High14"] = high14

        price_data.dropna()

        print(price_data)

        pass

data(stock=stock, start_date=start_date, end_date=end_date, candle_time= candle_time)