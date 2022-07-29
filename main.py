import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import accuracy_score
import yfinance as yf
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from data import data
import time

stock = input("enter stock: ")
print("The date should be in the form y-m-d")
start_date = input("enter start date: ")
end_date = input("enter end date: ")

data = data(stock, start_date, end_date)


#create trainingset
#copy price data to drop the close column
training = data.price_data.copy()
#drop price data
training_data = training.drop("Close", axis = 1)

#preparation for the analysis dropping Nan Lines
print(data.price_data)

#split data to attributes and labels
X = data.price_data[["RSI","Low14","High14", "K%", "Open", "Close", "Volume", "Adj Close"]]
y = data.price_data[["Prediction"]]


X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

feature_names = [f"feature {i}" for i in range(X.shape[1])]

Classifier = RandomForestClassifier(n_estimators = 100, oob_score = True, criterion="gini", random_state=0)

Classifier.fit(X_train, y_train.values.ravel())
#fixed the code https://stackoverflow.com/questions/34165731/a-column-vector-y-was-passed-when-a-1d-array-was-expected

y_pred = Classifier.predict(X_test)

#evaluation of the model computing accuracy score
print('Correct Prediction (%): ', accuracy_score(y_test, Classifier.predict(X_test), normalize = True) * 100.0)

#feature importance https://scikit-learn.org/stable/auto_examples/ensemble/plot_forest_importances.html
start_time = time.time()
importances = Classifier.feature_importances_
std = np.std([tree.feature_importances_ for tree in Classifier.estimators_], axis=0)
elapsed_time = time.time() - start_time

print(f"Elapsed time to compute feature importances: {elapsed_time:.3f} seconds")

forest_importances = pd.Series(importances, index=feature_names)

fig, ax = plt.subplots()
forest_importances.plot.bar(yerr=std, ax=ax)
ax.set_title("Feature importances using MDI")
ax.set_ylabel("Mean decrease in impurity")
fig.tight_layout()

plt.show()