import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier


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
print('Visualize data\nOpen\nHigh\nLow\nClose\nAdj Close\nVolume\nRSI\nHigh14\nLow14\nSMA')

#ask the user which data he wants to see
choice = input('enter your choice: ')

#create diagram
plt.figure(figsize=(16,8))
plt.title(choice)
plt.plot(price_data[[choice]])
plt.xlabel('Date', fontsize = 11)
plt.ylabel('Volume($)', fontsize=11)
plt.legend([choice])
plt.grid()
plt.show()

#random forest
#preparing training data
X = np.array(training_data)
Y = np.array(price_data["Close"])

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state=0)

X_test = np.array(X_test)
Y_test = np.array(Y_test)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

classifier = RandomForestClassifier(n_estimators=100, random_state=0)
classifier.fit(X_train, Y_train)
y_pred = classifier.predict(X_test)