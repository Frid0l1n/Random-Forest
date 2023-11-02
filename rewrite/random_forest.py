from data_test import data
from sklearn.ensemble import RandomForestRegressor

#import data from data.py
stock = input("enter stock: ")
start_date = input("enter start date it should have this form y-mo-d: ")
end_date = input("enter start date it should have this form y-mo-d: ")
stock_data_instance = data(stock= stock, start_date=start_date, end_date=end_date)

#Accessing the data to work with it


print(data)