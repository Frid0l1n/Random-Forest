import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns; sns.set()
from matplotlib.widgets import CheckButtons
import os

class Data:
    def __init__(self, stock, start_date, end_date):
        self.stock = stock
        self.start_date = start_date
        self.end_date = end_date

        # Fetch historical stock data using yfinance
        self.data = yf.download(stock, start=start_date, end=end_date)

        # Calculate indicators
        self.data["Daily_Return"] = self.data["Close"].pct_change() * 100
        self.data['SMA_50'] = self.data['Close'].rolling(window=50).mean()
        self.data["Standard_Deviation"] = self.data["Close"].rolling(window=50).std()
        self.data['Upper_Band'] = self.data['SMA_50'] + (self.data["Standard_Deviation"] * 2)
        self.data['Lower_Band'] = self.data['SMA_50'] - (self.data["Standard_Deviation"] * 2)
        self.data['EMA_12'] = self.data['Close'].ewm(span=12, adjust=False).mean()
        self.data['EMA_26'] = self.data['Close'].ewm(span=26, adjust=False).mean()
        self.data["MACD_Signal_Line"] = self.data["EMA_12"] - self.data["EMA_26"]
        self.data['VWAP'] = (self.data['Close'] * self.data['Volume']).cumsum() / self.data['Volume'].cumsum()
        period = 14
        self.data['ROC'] = (self.data['Close'].pct_change(periods=period)) * 100

        # Drop rows with NaN values
        self.data.dropna(inplace=True)

        # List of data for selection
        self.data_list = [self.data["Open"], self.data["Close"], self.data["Low"], self.data["High"], self.data["Adj Close"], self.data["Daily_Return"], self.data["SMA_50"], self.data["Standard_Deviation"], self.data["Upper_Band"], self.data["Lower_Band"], self.data["EMA_12"], self.data["MACD_Signal_Line"], self.data['VWAP']]

        # Plotting
        self.plot_data()

        # Save CSV
        self.save_csv()

    def plot_data(self):
        plot = input("Do you want to plot the data Y/N: ")

        if plot.upper() == "Y":
            fig, ax = plt.subplots(figsize=(12, 8))
            lines = []
            labels = []

            for idx, dataset in enumerate(self.data_list):
                line, = plt.plot(self.data.index, dataset, label=dataset.name)
                lines.append(line)
                labels.append(dataset.name)

            plt.xlabel('Date')
            plt.ylabel('Value')
            plt.title(f'Stock Data {self.stock}')
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

    def save_csv(self):
        file = input("Do you want to create a csv Y/N:")

        if file.upper() == "Y":
            file_name = f'{self.stock}.csv'
            self.data.to_csv(file_name, index=False)

            # Optionally specify a directory
            save_directory = "./data"
            os.makedirs(save_directory, exist_ok=True)
            save_file = os.path.join(save_directory, file_name)
            print(f"CSV saved to: {save_file}")

    def get_data(self):
        return self.data