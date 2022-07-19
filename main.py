import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from data import data

stock = input("enter stock: ")
print("The date should be in the form y-m-d")
start = input("enter start date: ")
end = input("enter end date: ")

data = data(stock, start, end)


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

X, y = make_classification(n_samples=60, n_features=4, n_informative=2, n_redundant=0, random_state=2, shuffle=False)

Classifier = RandomForestClassifier(n_estimators=4, random_state=0)
Classifier.fit(X,y)
y_pred = Classifier.predict(X)
print(y_pred)