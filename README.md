# Random Forest for Financial Machine Learning
## Version 1.0.0 (Publication Date: 09-18-2023)

## Table of Contents
1. [Introduction](#introduction)
2. [Data Preparation](#data-preparation)
   - [Types of Financial Data](#types-of-financial-data)
   - [Data Preparation Techniques](#data-preparation-techniques)
3. [Machine Learning Methods](#machine-learning-methods)
   - [Supervised Learning](#supervised-learning)
   - [Unsupervised Learning](#unsupervised-learning)
4. [Random Forest](#random-forest)
   - [Understanding Decision Trees and Overfitting](#understanding-decision-trees-and-overfitting)
   - [Introduction to Random Forest](#introduction-to-random-forest)
5. [Model Evaluation and Error Analysis](#model-evaluation-and-error-analysis)
6. [Sources](#sources)
   - [Books](#books)
   - [Websites](#websites)
   - [Videos](#videos)

## Introduction
My interest in machine learning, data analytics, and the stock market led me to choose financial machine learning as the topic for my high school final project. Despite having no prior experience with machine learning, I am committed to giving my best effort and documenting the entire process of building the model. The financial industry is evolving rapidly and seeks innovative ways to utilize machine learning for managing the risk of financial losses.

## Data Preparation
There are four essential types of financial data:

### Types of Financial Data

* **Fundamental Data**: Contains information found in regulatory filings and business analytics, reported quarterly. While fundamental data is highly regularized and available at a low frequency, it can be valuable when combined with other data types.

* **Market Data**: Encompasses all trading activities on exchanges, each leaving a characteristic footprint in the trading records. For instance, TWAP algorithms (Time-Weighted Average Price algorithms) leave distinct footprints.

* **Analytics**: Processed data providing in-depth analysis of various companies. Investment banks often sell this valuable analysis, which includes assessments of activities, competition, outlook, etc., with the signal already extracted from raw data.

* **Alternative Data**: Mainly produced by individuals or communities like [Wallstreetbets](https://www.reddit.com/r/wallstreetbets) who discuss and influence lesser-known stocks like 'Gamestop'. Alternative data is also sourced from various journals or Google searches.

### Data Preparation Techniques

For data preparation, we utilize the open-source Python library [pandas](https://pandas.pydata.org/docs/index.html). We fetch data from Yahoo Finance, an excellent source for reliable stock market movements and prices in the form of a CSV file. Most ML algorithms require data in a regularized format, often assuming a tabular representation of the extracted data. Given the dynamic nature of the market, processing the data at constant time intervals isn't optimal. Therefore, we log the data at regular time intervals, such as every minute or every day. Our dataset includes Date, Volume, Open, Close, High, Low, and Adj. Close. We further calculate technical indicators like RSI, Stochastic Oscillator, William Percent Range, and Moving Average Convergence Divergence to gather insights into future stock movements. To visualize stock movements, we employ the [matplotlib](https://matplotlib.org/) library.

# Machine Learning Methods

There are Various Machine Learning Algorithms out there, as you probably know the algorithm which is used in this Project is also known as a Random Forest Classifier. More about that in the subchapter [Supervised Learning](#supervised-learning).

### Supervised Learning
* Classification
* Regression

### Unsupervised Learning
* Clustering

## Common Errors in ML Models
ML models often suffer from three main errors:

* **Bias**: Arises from unrealistic assumptions, causing the algorithm to overlook crucial relations between features and outcomes. High bias leads to the algorithm being "underfit" ([Learn more](https://www.ibm.com/cloud/learn/underfitting)).

* **Variance**: Results from sensitivity to minor dataset changes, causing the algorithm to overfit the dataset. High variance leads to significantly different predictions with minimal dataset alterations, mistaking noise for a signal.

* **Noise**: Caused by the variance of observed values, unpredictable changes, or measurement errors, impossible to be explained by any model.

## Random Forest
Decision trees are known to be prone to overfitting, resulting in high forecast variance. The Random Forest (RF) method was designed to produce ensemble forecasts with lower variance.

### Understanding Decision Trees and Overfitting

### Introduction to Random Forest

# Model Evaluation and Error Analysis

## Sources
### Books
1. [Advances in Financial Machine Learning](https://www.amazon.com/Advances-Financial-Machine-Learning-Marcos/dp/1119482089) (Marcos Lopez de Prado, published 23rd January 2018)
2. [Applied Quantitative Finance using Python for Financial Analysis](https://www.amazon.com/Applied-Quantitative-Finance-Financial-Analysis/dp/1803231879) (Mauricio Garita, published 3rd September 2021)
3. [The Elements of Statistical Learning: Data Mining, Inference, and Prediction](https://web.stanford.edu/~hastie/Papers/ESLII.pdf) (Trevor Hastie, Robert Tibshirani, Jerome Friedman, 2001)
4. [Introduction to Machine Learning with Python](https://www.amazon.com/Introduction-Machine-Learning-Python-Scientists/dp/1449369413) (Andreas C. Müller, Sarah Guido, published 2016)

### Websites
1. [Scikit-learn](https://scikit-learn.org/stable/)
2. [Pandas](https://pandas.pydata.org/)
3. [Random Forest Regression](https://levelup.gitconnected.com/random-forest-regression-209c0f354c84)
4. [Pandas Moving Average by Group](https://www.statology.org/pandas-moving-average-by-group/)

### Videos