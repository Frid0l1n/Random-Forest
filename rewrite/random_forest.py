from data_test import data
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pandas as pd
import yfinance as yf

# Get user inputs
stock = input("Enter stock: ")
start_date = input("Enter start date (y-mo-d): ")
end_date = input("Enter end date (y-mo-d): ")

# Fetch the data
df = data(stock=stock, start_date=start_date, end_date=end_date)
print("Fetched data:", df)  # Debugging line to check the structure of df

print(type(data))

# Check if df is already a DataFrame
if isinstance(df, pd.DataFrame):
    data = df
else:
    data = pd.DataFrame(df)

class Algorithm:
    def __init__(self, data):
        self.data = data
        self.regressor = RandomForestRegressor(max_depth=3, random_state=0)

    def train(self):
        if not isinstance(self.data, pd.DataFrame):
            raise TypeError("Data should be a pandas DataFrame")
        
        x = self.data[["Open", "High", "Low", "ROC"]]
        y = self.data["Close"]
        
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
        
        self.regressor.fit(x_train, y_train)
        
        predictions = self.regressor.predict(x_test)
        print("Predictions:", predictions)

        return predictions

# Initialize and train the model
model = Algorithm(data=data)
model.train()

