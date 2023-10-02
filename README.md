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
   - [Librarys](#librarys)
   - [Books](#books)
   - [Websites](#websites)
   - [Videos](#videos)

## Introduction
My interest in machine learning, data analytics, and the stock market led me to choose financial machine learning as the topic for my high school final project. Despite having no prior experience with machine learning, I am committed to giving my best effort and documenting the entire process of building the model. The financial industry is evolving rapidly and seeks innovative ways to utilize machine learning for managing the risk of financial losses.

## Data Preparation
As we already know no one wants to deal with unstructured data that means we have to structure it. This project contains four essential types of financial data:

### Types of Financial Data

Financial Data is usually divided into four main categories, these four categories are listed below. As we already know, it takes some quality datasets to tech machine learning algorithms how to make accurate predictions. These four financial datatypes describe the data that is extracted and fitted into a dataframe to train a ML system.

* **Fundamental Data**: Contains information found in regulatory filings and business analytics, reported quarterly. While fundamental data is highly regularized and available at a low frequency, it can be valuable when combined with other data types.

* **Market Data**: Encompasses all trading activities on exchanges, each leaving a characteristic footprint in the trading records. For instance, TWAP algorithms (Time-Weighted Average Price algorithms) leave distinct footprints.

* **Analytics**: Processed data that provides in-depth analysis of various companies. Investment banks often sell this valuable analysis, which includes assessments of activities, competition, outlook, etc., with the signal already extracted from raw data.

* **Alternative Data**: Mainly produced by individuals or communities like [Wallstreetbets](https://www.reddit.com/r/wallstreetbets) who discuss and influence lesser-known stocks like 'Gamestop'. Alternative data is also sourced from various journals or Google searches.

### Data Preparation Techniques

For data preparation, we utilize the open-source Python library [pandas](https://pandas.pydata.org/docs/index.html). We fetch data from Yahoo Finance, an excellent source for reliable stock market movements and prices in the form of a CSV file. Most ML algorithms require data in a regularized format, often assuming a tabular representation of the extracted data. Given the dynamic nature of the market, processing the data at constant time intervals isn't optimal. Therefore, we log the data at regular time intervals, such as every minute or every day. Our dataset includes Date, Volume, Open, Close, High, Low, and Adj. Close. We further calculate technical indicators like RSI, Stochastic Oscillator, William Percent Range, and Moving Average Convergence Divergence to gather insights into future stock movements. To visualize stock movements, we employ the [matplotlib](https://matplotlib.org/) library.

# Machine Learning Methods

There are Various Machine Learning Algorithms out there, as you probably know the algorithm which is used in this Project is also known as a Random Forest Classifier. More about that in the subchapter [Supervised Learning](#supervised-learning).

### Supervised Learning
* Classification (Classification is a supervised machine learning method where the model tries to predict the correct label of a given input data. In our case it woudl be will the stock rise or fall in price)
* Regression (ML Regression is a technique for investigating a relationship between independant variables or features and a dependant variable or outcome, it is manly used in algorithms which have to predict continous outcomes.)

### Unsupervised Learning
* Clustering (A lot of input data is given to Clustering Algorithms but without labels, the algorithm has to find groupings to create a relation.)


## Common Errors in ML Models
ML models often suffer from three main errors:

* **Bias**: Arises from unrealistic assumptions, causing the algorithm to overlook crucial relations between features and outcomes. High bias leads to the algorithm being "underfit" ([Learn more](https://www.ibm.com/cloud/learn/underfitting)).

* **Variance**: Results from sensitivity to minor dataset changes, causing the algorithm to overfit the dataset. High variance leads to significantly different predictions with minimal dataset alterations, mistaking noise for a signal.

* **Noise**: Caused by the variance of observed values, unpredictable changes, or measurement errors, impossible to be explained by any model.

## Random Forest
Decision trees are known to be prone to overfitting, resulting in high forecast variance. The Random Forest (RF) method was designed to produce ensemble forecasts with lower variance.

### Understanding Decision Trees and Overfitting
Decision Trees often used in differen ML Systems but are one of the simplest algorithms in machine learning as well as easy to interpret meanwhile giving powerfull prediction. The decision tree is built from the bottom to the top leaves, to build the tree our dataset is split into two the training set to build the tree and the testing set is used to measure the performance of the tree. Decision Trees are prone to overfit, it occurs if the model fits to closely to the training data this can lead to miss predictions, caused by overfitting of the tree. Because Decision trees are known to overfit Pruning was found, purning is a technique that removes parts of the decision tree and prevents it from growing up to the leavs, data which is evaluated by a pruned tree is less likely to be miss interpreted.

### Introduction to Random Forest
Random forest is a widely used ML technique trademarked by Leo Breiman and Adele Cutler, which combines the output of multiple decision trees to reach a single result. It could be used as Classifier as Well as Regressor, this project uses the classifier. A big plus point is that the model is trained rapidly, hence to the fact that he owns multiple Decision Trees the evaluation could run paralized that means the analysis is made in a short time.

# Model Evaluation and Error Analysis

## Sources
Here is a list of sources used for this project.
### librarys
1. [Pandas](https://pandas.pydata.org/) (The Pandas development team, publisher Zendoo, version latest)
2. [Numpy](https://numpy.org/) (Charles R. Harris, K. Jarrod Millman, Stéfan J. van der Walt, Ralf Gommers, Pauli Virtanen, David Cournapeau, Eric Wieser, Julian Taylor, Sebastian Berg, Nathaniel J. Smith, Robert Kern, Matti Picus, Stephan Hoyer, Marten H. van Kerkwijk, Matthew Brett, Allan Haldane, Jaime Fernández del Río, Mark Wiebe, Pearu Peterson, Pierre Gérard-Marchant, Kevin Sheppard, Tyler Reddy, Warren Weckesser, Hameer Abbasi, Christoph Gohlke & Travis E. Oliphant, published 09.x.2020)
3. [yfinance](https://pypi.org/project/yfinance/) (yfinance is a community effort, data belongs to Yahoo)
4. [Sklearn](https://scikit-learn.org/stable/) (Pedregosa, F. and Varoquaux, G. and Gramfort, A. and Michel, V. and Thirion, B. and Grisel, O. and Blondel, M and Prettenhofer, P. and Weiss, R. and Dubourg, V. and Vanderplas, J. and Passos, A. and Cournapeau, D. and Brucher, M. and Perrot, M. and Duchesnay, E.,published 2011)
5. [Matplotlib](https://matplotlib.org/) (Hunter , J. D., published 2007)
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

1. [The Machine Learning Revolution by Marcos López de Prado](https://www.youtube.com/watch?v=7i0RFtZu4Ek) (Andres Oloms, published 23.06.2019)

work in progress
