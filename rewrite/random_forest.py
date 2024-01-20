from data_test import data
from sklearn.ensemble import RandomForestRegressor

#import data from data.py
stock = input("enter stock: ")
start_date = input("enter start date it should have this form y-mo-d: ")
end_date = input("enter start date it should have this form y-mo-d: ")
stock_data_instance = data(stock= stock, start_date=start_date, end_date=end_date)

#Accessing the data to work with it

class algorithm():
    def __init__(self, data) -> None:
        self.data = data
        regressor = RandomForestRegressor(n_estimators=100, max_depth=None)
        output = regressor(data)
        print(output)

        return output

algorithm(data=data)