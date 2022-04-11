# Random forest for financial machine learning

**Version 1.0.0**

My interest in machine Learning, data analytics and the Stockmarket led me to choose the topic financial machine learning for my final project of High School. I've no experience with machine learning but i'll try my best and document the whole process of building the model. The financial industry is growing day by day and is looking for ways to use machine learning for managing the risk of loosing money.


## Data preperation
There are four essential types of financial data.
* [Fundamental data](https://www.investopedia.com/terms/f/fundamentalanalysis.asp) contains information that can be found in regulator filings and buisnes analytics.    Accaunting data which is reported quarterly. Fundamental data is extremly regularized and only in low frequency available but it maybe useful in combination with other data types.

* [Market data](https://www.ig.com/en/glossary-trading-terms/market-data-definition) includes all trading activity that takes place in an exchange. Every market participant leaves a characteristic footprint in the trading records. As an example TWAP algorithms leave a very particular footprint.

* Analytics is already processed for you in a particular way. Many investment banks are selling these valuable indepth analisys of various companys. Those banks or companys analyse the activities, competition, outlook etc. The signal is already extracted from the raw data.

* Alternative Data is mainly produced by individuals, [Wallstreetbets](https://www.reddit.com/r/wallstreetbets) is such an alternative data producer these guys are pushing litle stocks as an example 'Gamestop'. Alternative data is also produced by different journals or google searches.

| Fundamental data| Market Data                   | Analytics               | Alternative Data     |
| --------------- | ----------------------------- | --------------------    | ---------------------|
| Assets          | Price/yield/implied volatility| Analyst recommendations |Satellite/CCTV images |
| Liabilities     | Volume                        | Credit ratings          |Google searches       |
| Sales           | Dividend/coupons              | Earning expectations    |Socialmedia chats     |
| Cost/earnings   | Open interest                 | News sentiments         |Metadata              |
| Macro variables | Quotes/cancellations          | ....                    |....                  |
| ....            | ....                          |                         |                      |

For data preparation we use the open source python library [pandas](https://pandas.pydata.org/docs/index.html). To get the data we use yahoo finance, it's the best way to aquire reliable stock market movements and prices in form of a csv file. Most of the ML algorithms need data in a regularized format. Most of the algorithms assume a table representation of the extracted data. It isn't the smartest way to process the data in a constant time intervall because the market couldn't be represented as a constat time intervall system (Open hour is mostly more active than the hour in the noon, at midnight mostly futures are traded by CPU). The data shuld be loged in a time intervall this means every minute or every day. Our data set incluedes Date, Volume, Open, Close High, Low and Adj. Close. The File contains various columns we want to calculate the RSI, Stochiastic Oscilator, William percent range as well as the Moving Average Convergence Divergence. These are all technical indicators and should provide us various information about the future stock movement. For the visualization of the stock movement we used the library [matplotlib](https://matplotlib.org/).

## Modelling
ML models generally suffer from three main errors

* Bias: This error is caused by unrealistic assumptions. When Bias is high the algorithm failed to recognize important relations between features and outcomes. In this situation, the algorithm is said to be ["underfit"](https://www.ibm.com/cloud/learn/underfitting)

* Variance: This error is caused by sensivity to small changes in the data set. When the variance is high, the algorithm has overfit the dataset. Minimal changes in the dataset can produce widly different predictions. Rather than modeelling the gerneral patzterns in the dataset, the algorithm has mistaken [noise](https://deepchecks.com/glossary/noise-in-machine-learning/) with signal.

* Noise: This error is caused by the variance of the observed values, unpredictable changes or measurement errors. Can't be explained by any model.

#### Random Forest
Decision trees are known to be prone to overfitting this means the variance of the forecast is really high. The random forest (RF) method was designed to produce ensemble forecast with lower variance.

#### Sources
Advances in Financial Machine Learning (Marcos Lopez de Prado published in 23. January 2018)