from typing_extensions import Self
import yfinance as yf
import pandas as pd

stock = input("Enter stock: ")
start_date = input("Enter start date: ")
end_date = input("Enter end date: ")

class data:
    def __init__(self, stock, start_date, end_date):

        self.stock = stock
        self.start_date = start_date
        self.end_date = end_date
        
        ticker = yf.Ticker(stock)
        data = ticker.history(period="1mo")
        
        print(data)

        pass

data(stock=stock, start_date=start_date, end_date=end_date)