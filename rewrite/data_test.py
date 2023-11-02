import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns; sns.set()
from matplotlib.widgets import CheckButtons

class data:

    def __init__(self, stock, start_date, end_date):
        self.stock = stock
        self.start_date = start_date
        self.end_date = end_date

        # Fetch historical stock data using yfinance
        data = yf.download(stock, start=start_date, end=end_date)

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

        #list data for selection
        data_list = [data["Open"], data["Close"], data["Low"], data["High"], data["Adj Close"], data["Daily_Return"], data["SMA_50"], data["Standard_Deviation"], data["Upper_Band"], data["Lower_Band"], data["EMA_12"], data["MACD_Signal_Line"], data['VWAP']]

        plot = input("Do you want to plot the data Y/N: ")

        if plot.upper() == "Y":
            fig, ax = plt.subplots(figsize=(12, 8))
            lines = []
            labels = []

            for idx, dataset in enumerate(data_list):
                line, = plt.plot(data.index, dataset, label=data_list[idx].name)
                lines.append(line)
                labels.append(data_list[idx].name)

            plt.xlabel('Date')
            plt.ylabel('Value')
            plt.title(f'Stock Data {stock}')
            plt.legend()

            # Create check buttons to toggle visibility of each line
            ax_check = plt.axes([0.85, 0.1, 0.15, 0.8])
            check = CheckButtons(ax_check, labels, [True] * len(labels))

            def func(label):
                index = labels.index(label)
                lines[index].set_visible(not lines[index].get_visible())
                plt.draw()

            check.on_clicked(func)
            plt.show()
        else:
            print("Next step")

        #ask if they want to create a csv file or print the data to console
        file = input("Do you want to create a csv Y/N:")

        if file.upper() == "Y":
            df = pd.DataFrame(data)
            csv_file_path = f'{stock}.csv'
            df.to_csv(csv_file_path)
        else:
            print(data)
        
        return data