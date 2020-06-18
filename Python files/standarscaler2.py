# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 13:53:39 2019

@author: user
"""

from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv(r"D:\Datasets\Churn_Modelling.csv")
data2 = data.drop(['RowNumber', 'CustomerId', 'Surname'], axis=1)
corr = data2.corr(method='pearson')
plt.figure(figsize=(10, 10))
sns.heatmap(corr, cmap='coolwarm', annot=True)

# if we pass every data , those not affecting will only increase computational time

ip = data2.drop(['Exited'], axis=1)
data.columns

# Label encoding -> gives numerical coding to it


# label encoder


le1 = LabelEncoder()
ip.Gender = le1.fit_transform(ip.Gender)
print(ip.tail())
# to print last 5 values


op = data2['Exited']
ip.head()

le2 = LabelEncoder()
ip.Geography = le2.fit_transform(ip.Geography)

#le2 = LabelEncoder()
# ip.G

ohe = OneHotEncoder(categorical_features=[1, 2])
ip = ohe.fit_transform(ip).toarray()

# converted to an array to make space for the array space


xtr, xts, ytr, yts = train_test_split(ip, op, test_size=0.2)

plt.boxplot(xtr)
plt.show()

# scaler scales to a same scale value by Normalization

sc = StandardScaler()
sc.fit(xtr)


# in fit it calculates the mean and sd
# in fit transform it replaces as well

xtr = sc.transform(xtr)
xts = sc.transform(xts)

plt.boxplot(xtr)
plt.show()

# outliers are the clusters outside the box

model = LogisticRegression()
model.fit(xtr, ytr)

y_pred = model.predict(xts)
print(confusion_matrix(yts, y_pred))

# logistics regression is not accurate

model.score(xts, yts)
