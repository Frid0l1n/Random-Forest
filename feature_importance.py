import pandas_datareader as web
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import Ridge

stock = input("enter stock: ")

price_data = web.DataReader(stock, data_source = "yahoo", start="2011-01-01", end = "2021-01-01")

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
price_data['Change In Price'] = down_df['Change In Price']
#add the new lines to the dataframe
price_data['Change In Price'] = up_df['Change In Price']
price_data['RSI'] = relative_strength_index


#stochiastic oscilator
A = price_data["Change In Price"]-price_data["Low14"]
B = price_data["High14"]-price_data["Low14"]
K_percent = A/B*100


price_data["K%"] = K_percent

price_data = price_data.dropna()

print(price_data)

X = price_data[["High", "Low", "Open", "Volume", "Change In Price", "Low14", "High14", "RSI"]]
y = price_data[["Close", "Adj Close"]]

X, y = make_classification(n_samples=10, n_features=2, n_informative=2, n_redundant=0, random_state=0, shuffle=False)
clf = RandomForestClassifier(max_depth=2, random_state=0)
clf.fit(X, y)

y_pred = clf.predict(price_data[["Close", "Adj Close"]])

print(y_pred)