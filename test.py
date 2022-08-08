from re import X
import yfinance as yf

msft = yf.Ticker("msft")

x = msft.history(period="max", interval="1mo")

print(x)