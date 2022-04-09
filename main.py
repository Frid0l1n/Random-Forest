import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#import the data and create Dataframe
df = pd.read_csv("NVDA.csv", skip_blank_lines=True)
price_data = df[['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]

#format output
#pd.set_option("display.max_rows", None,"display.max_columns", None)
#calculate the change in price
price_data['Change In Price'] = price_data['Close'].diff()


"""
____________________________________________________________________________________________________________________________________________________________________
"""

#calculate the rsi
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
#add the new lines to the dataframe
price_data['Change In Price'] = down_df['Change In Price']
price_data['Change In Price'] = up_df['Change In Price']
price_data['RSI'] = relative_strength_index


""""
____________________________________________________________________________________________________________________________________________________________________
"""
#for the stochiastic oscilator we need a time period given the n=14

n = 14

low_14, high_14 = price_data[['Low']].copy(), price_data[['High']].copy()

#rolling function for min and max
low_14 = low_14['Low'].transform(lambda x: x.rolling(window = n).min())
high_14 = high_14['High'].transform(lambda x: x.rolling(window = n).max())

#calculating the stochiastic oscilator
K_percent = 100*((price_data['Close']-low_14)/(high_14-low_14))

#add the gatherd information to the dataframe
price_data['Low 14'] = low_14
price_data['High 14'] = high_14
price_data['K Percent'] = K_percent

"""
______________________________________________________________________________________________________________________________________________________________________
"""

#williams calculation
n = 14
#define the low_14, high_14 column and copy it
low_14, high_14 = price_data[['Low']].copy(), price_data[['High']].copy()
#rolling function for min and max
low_14 = low_14['Low'].transform(lambda x: x.rolling(window = n).min())
high_14 = high_14['High'].transform(lambda x: x.rolling(window = n).max())
#calculate r percent
R_percent = ((high_14 - price_data['Close'])/(high_14 - low_14))* -100

price_data['R Percent'] = R_percent

"""
______________________________________________________________________________________________________________________________________________________________________
"""

plt.figure(figsize=(16,8))
plt.title('RSI')
plt.plot(price_data['R Percent'])
plt.xlabel('Date', fontsize=18)
plt.ylabel('Close Price USD($)', fontsize=11)
plt.show()