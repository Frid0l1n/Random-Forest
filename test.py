import yfinance as yf
import pandas as pd

class data:
    def __init__(self, stock, start, end, interval):
        self.stock = stock
        self.start = start
        self.end = end
        self.interval = interval
        x = yf.Ticker(stock)
        data = x.history(start= start, end = end, interval=interval)
        
        data["Change In Price"] = data["Close"].diff()
        delta = data["Change In Price"].diff(1)
        delta.dropna(inplace = True)

        positive = delta.copy()
        negative = data.copy()

        positive[positive < 0] = 0
        negative[negative > 0] = 0

        days = 14

        average_gain = positive.rolling(window=days).mean()
        average_loss = negative.rolling(window=days).mean()

        relative_strength = average_gain / average_loss
        data["RSI"] = 100.0 - (100.0 / (1.0 + relative_strength))

        print(data)

        


stock = input("enter stock: ")
start = input("enter start date: ")
end = input("enter end date: ")
interval = input("enter interval: ")

data(stock, start, end, interval)