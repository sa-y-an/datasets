# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 11:01:27 2019

@author: user

"""

# Credit Card Score

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r"D:\Datasets\creditcard.csv\creditcard.csv")

#data['Time'].dtype

ip = data.drop(['Class'],axis=1)
op = data.Class

from sklearn.model_selection import  train_test_split
xtr , xts , ytr , yts = train_test_split(ip,op,test_size=0.2)

from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB

modelLR = LogisticRegression()
modelNB = GaussianNB()

modelLR.fit(xtr,ytr)
modelNB.fit(xtr,ytr)

from sklearn.metrics import confusion_matrix
predLR = modelLR.predict(xts)
predNB = modelNB.predict(xts)
print(confusion_matrix(yts,predLR))
#print(predNB)