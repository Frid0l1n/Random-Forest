import yfinance as yf

#create class to acces data easy
class data:
    def __init__(self, input_stock, input_timespan):
        #define the input variables for the price_data
        self.stock = input_stock
        self.timespan = input_timespan
        #select the right stock from the class input
        price_data = yf.Ticker(input_stock)
        #acces the data about the stock
        price_data = price_data.history(period=input_timespan)
        #calculate the change in price using the python diff function
        price_data["Change In Price"] = price_data["Close"].diff()

        print(price_data)

x = input("enter stock: ")
y = input("enter stock: ")

data(x,y)