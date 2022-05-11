import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import r2_score
from data import data



stock = input("enter stock: ")
print("The date should be in the form y-m-d")
start = input("enter start date: ")
end = input("enter end date: ")

data = data(stock, start, end)

print(data.price_data)


#create trainingset
#copy price data to drop the close column
training = data.price_data.copy()
#drop price data
training_data = training.drop("Close", axis = 1)
#Visualize the Data
print('Visualize data\nOpen\nHigh\nLow\nClose\nAdj Close\nVolume\nRSI\nHigh14\nLow14\nSMA')
print("to leave visualize the data press X")

"""
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
plt.plot(data=[list_technical_analysis], label = list_technical_analysis)
plt.xlabel("Date", fontsize = 11)
plt.ylabel('Volume($)', fontsize=11)
plt.legend(list_technical_analysis)
plt.grid()
plt.show()
"""

#preparation for the analysis dropping Nan Lines
print(data.price_data)

#split data to attributes and labels
X = data.price_data[["Change In Price", "RSI","Low14","High14"]]
y = data.price_data[["Close"]]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

regressor = RandomForestRegressor(n_estimators=4, random_state=0)
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
print(y_pred)