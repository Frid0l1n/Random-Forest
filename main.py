from pickle import FALSE
from re import X
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#import the data and create Dataframe
df = pd.read_csv("./stocks/NVDA.csv", skip_blank_lines=True)
price_data = df[['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]

#format output
#pd.set_option("display.max_rows", None,"display.max_columns", None)
#calculate the change in price
price_data['Change In Price'] = price_data['Close'].diff()


#calculate the rsi
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

#14 days low/14 days high
n = 14

low_14, high_14 = price_data[['Low']].copy(), price_data[['High']].copy()
low14 = low_14['Low'].transform(lambda x: x.rolling(window = n).min())
high14 = high_14['High'].transform(lambda x: x.rolling(window = n).max())
price_data['Low14'] = low14
price_data['High14'] = high14

#calculate simple moving average
n = 14
#calculate the average of the 14 days
sma = price_data['Close'].transform(lambda x: x.ewm(span = n).mean())
price_data["SMA"] = sma


#create trainingset
#copy price data to drop the close column
training = price_data.copy()
#drop price data
training_data = training.drop("Close", axis = 1)
#Visualize the Data
print('Visualize data\nOpen\nHigh\nLow\nClose\nAdj Close\nVolume\nRSI\nHigh14\nLow14\nSMA\X')

#ask the user which data he wants to see
list_stocks = []
while True:
    choice = input('enter your choice: ')
    list_stocks.append(choice)
    if choice == "X":
        break

list_stocks.remove(list_stocks[len(list_stocks)-1])

#create diagram
plt.figure(figsize=(16,8))
plt.title([list_stocks])
plt.plot(price_data[list_stocks])
plt.xlabel('Date', fontsize = 11)
plt.ylabel('Volume($)', fontsize=11)
plt.legend([choice])
plt.grid()
plt.show()