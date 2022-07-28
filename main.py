import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import accuracy_score
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
X = data.price_data[["RSI","Low14","High14"]]
y = data.price_data[["Prediction"]]


X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

Classifier = RandomForestClassifier(n_estimators = 100, oob_score = True, criterion="gini", random_state=0)

Classifier.fit(X_train, y_train.values.ravel())
#fixed the code https://stackoverflow.com/questions/34165731/a-column-vector-y-was-passed-when-a-1d-array-was-expected

y_pred = Classifier.predict(X_test)

#evaluation of the model computing accuracy score
print('Correct Prediction (%): ', accuracy_score(y_test, Classifier.predict(X_test), normalize = True) * 100.0)