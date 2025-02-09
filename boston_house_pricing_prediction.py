# -*- coding: utf-8 -*-
"""Boston House Pricing Prediction

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lxbPTdIQFiji51fPeri4ybs4wUyKKtH7

*importing dependences*
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics
from xgboost import XGBRegressor

"""Data collection and analysis"""

#import data
boston_house_price = pd.read_csv('/content/boston.csv')

boston_house_price.head()

#add prices to the dataframe
boston_house_price['price'] = boston_house_price['MEDV']
boston_house_price.head()

#remove the MEDV column
boston_house_price.drop(['MEDV'], axis=1, inplace=True)
boston_house_price.head()

boston_house_price.shape

#check for missing values
boston_house_price.isnull().sum()

#statistical measures off the dataset
boston_house_price.describe()

"""Understanding the correlations between various fields"""

# check for positive correlations and negative correlations
correlation = boston_house_price.corr()

#construct a heat map to understand the correlation
plt.figure(figsize=(10,10))
sns.heatmap(correlation, cbar=True, square=True, fmt='.2f', annot=True, annot_kws={'size':8}, cmap='Reds')

"""Split the data and the target(meaning the price)"""

X = boston_house_price.drop(['price'], axis=1)
Y = boston_house_price['price']

print(X)
print(Y)

"""Split the data into train and test data"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 2)

print(X_train.shape, X_train.shape, X_test.shape)

"""Model Training using XGBoost Regressor"""

#loading the model
model = XGBRegressor()

#fit the training data X_train
model.fit(X_train, Y_train)

"""Evaluation of model; we cannot use accuracy scores for regression models, rather we use mathematical metrics like absolute values"""

#Prediction on training data
X_train_data_prediction = model.predict(X_train)

print(X_train_data_prediction)

#R squared error measure
r_score = metrics.r2_score(Y_train, X_train_data_prediction)
print("R squared error = ", r_score)

#mean absolute error
m_score = metrics.mean_absolute_error(Y_train, X_train_data_prediction)
print('Mean Absolute Error=', m_score)

#apply prediction on the test data
X_test_data_prediction = model.predict(X_test)
print(X_test_data_prediction)

#error measures on test data
r_score = metrics.r2_score(Y_test, X_test_data_prediction)
print("R squared error = ", r_score)

#mean absolute error
m_score = metrics.mean_absolute_error(Y_test, X_test_data_prediction)
print('Mean Absolute Error=', m_score)

"""Compare the Actual and predicted data"""

#comparing actual and predicted data
plt.scatter(Y_train, X_train_data_prediction)
plt.xlabel("Actual House Prices")
plt.ylabel("Predicted House Prices")
plt.title("Actual House Prices vs Predicted House Prices")
plt.show()

