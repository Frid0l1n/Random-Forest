import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from data import data
import openpyxl as xls


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

#preparation for the analysis dropping Nan Lines
print(data.price_data)

#split data to attributes and labels
X = data.price_data[["Low","High","Close","Volume","Change In Price", "RSI","Low14","High14"]]
y = data.price_data[["Close"]]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

regressor = RandomForestRegressor(n_estimators=4, random_state=0)
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
print(y_pred)

#convert ndray to dataframe
print(type(y_pred))
df = pd.DataFrame(y_pred, columns= ["Prediction"])
print(type(df))

#write the output to excel file
excel_file = pd.ExcelWriter("prediction.xlsx")
df.to_excel(excel_file)
excel_file.save()