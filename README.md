# Random forest for financial machine learning
My interest in machine Learning, data analytics and the Stockmarket led me to choose the topic financial machine learning for my final project of the High School. I've no experience with machine learning but i'll try my best and document the whole process of building the model. The financial industry is growing day by day and is looking for ways to use machine learning for managing the risk of loosing money.

## Data preperation
There are four essential types of financial data.
Fundamental data contains information that could be found in regulatori filings and buisnes analytics. Accaunting data which is reported quarterly. Fundamental data is extremly regulized and low frequency but it maybe useful in combination with other data types.

| Fundamental data| Market Data                   | Analytics               | Alternative Data     |
| --------------- | ----------------------------- | --------------------    | ---------------------|
| Assets          | Price/yield/implied volatility| Analyst recommendations | Satellite/CCTV images|
| Liabilities     | Volume                        | Credit ratings          |Google searches       |
| Sales           | Dividend/coupons              | Earning expectations    |Socialmedia chats     |
| Cost/earnings   | Open interest                 | News sentiment          |Metadata              |
| Macro variables | Quotes/cancellations          | ....                    |....                  |
| ....            | ....                          |                         |                      |
For Data preparation we use the open source python library [pandas](https://pandas.pydata.org/docs/index.html). To get the data we use yahoo finance, it's the best way to aquire reliable stock market movements and prices in form of a csv file. The File contains various columns we want to calculate the RSI, Stochiastic Oscilator, William percent range as well as the Moving Average Convergence Divergence. These are all technical indicators and should provide us various information about the future stock movement.
