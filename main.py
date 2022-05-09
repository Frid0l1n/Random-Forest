import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import accuracy_score, r2_score
from sklearn.metrics import r2_score


#get user input and create data frame
stock = input("enter stock: ")
time_span = input("enter time span: ")
input_data = yf.Ticker(stock)
price_data = input_data.history(period=time_span, interval="1d")

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

#stochiastic oscilator
X_stochastic = price_data["Close"]-price_data["Low14"]
Y_stochiastic = price_data["High14"]-price_data["Low14"]

K_percent = (X_stochastic/Y_stochiastic)*100
price_data["%K"] = K_percent


#create trainingset
#copy price data to drop the close column
training = price_data.copy()
#drop price data
training_data = training.drop("Close", axis = 1)
#Visualize the Data
print('Visualize data\nOpen\nHigh\nLow\nClose\nAdj Close\nVolume\nRSI\nHigh14\nLow14\nSMA')
print("to leave visualize the data press X")

#ask the user which data he wants to see
list_technical_analysis = []
while True:
    choice = input('enter your choice: ')
    list_technical_analysis.append(choice)
    if choice == "X":
        break

list_technical_analysis.remove(list_technical_analysis[len(list_technical_analysis)-1])
plt_title = ", ".join(map(str, list_technical_analysis))
print(plt_title)
#create diagram
plt.figure(figsize=(16,8))
plt.title(plt_title)
plt.plot(price_data[list_technical_analysis], label = list_technical_analysis)
plt.xlabel("Date", fontsize = 11)
plt.ylabel('Volume($)', fontsize=11)
plt.legend(list_technical_analysis)
plt.grid()
plt.show()

#preparation for the analysis dropping Nan Lines
price_data = price_data.dropna()
print(price_data)

#split data to attributes and labels
X = price_data[["Change In Price", "RSI","Low14","High14","SMA"]]
y = price_data[["Close"]]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

regressor = RandomForestRegressor(n_estimators=4, random_state=0)
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
print(y_pred)