import yfinance as yf
import pandas as pd

# Get stock to analyze
stock = input("Enter stock symbol: ")
stock_data = yf.Ticker(f"{stock}")

# Fetch historical stock data using yfinance
data = yf.download(stock, start="2017-01-01", end="2019-04-30")

# Calculate daily return
data["Daily_Return"] = data["Close"].pct_change() * 100

# Calculate a 50-day simple moving average with Bollinger Bands
data['SMA_50'] = data['Close'].rolling(window=50).mean()

# Calculate standard deviation
data["Standard_Deviation"] = data["Close"].rolling(window=50).std()

# Calculate Bollinger Bands
data['Upper_Band'] = data['SMA_50'] + (data["Standard_Deviation"] * 2)
data['Lower_Band'] = data['SMA_50'] - (data["Standard_Deviation"] * 2)

# Calculate a 12-day exponential moving average
data['EMA_12'] = data['Close'].ewm(span=12, adjust=False).mean()
data['EMA_26'] = data['Close'].ewm(span=26, adjust=False).mean()

data["MACD_Signal_Line"] = data["EMA_12"] - data["EMA_26"]

#VWAP
data['VWAP'] = (data['Close'] * data['Volume']).cumsum() / data['Volume'].cumsum()

# Calculate Rate of Change (ROC)
period = 14  # You can adjust this period as needed
data['ROC'] = (data['Close'].pct_change(periods=period)) * 100

# Drop rows with NaN values
data.dropna(inplace=True)

print(data)