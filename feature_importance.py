from numpy import DataSource
import pandas_datareader as web

ticker = web.DataReader("NVDA", data_source = "yahoo", start = "2011-01-01", end = "2012-01-01")
print(ticker)