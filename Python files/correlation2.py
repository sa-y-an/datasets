# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 09:50:52 2019

@author: user
"""

import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = pd.read_excel(r"D:\Datasets\ENB2012_data.xlsx")

corr = data.corr(method='pearson')

plt.figure(figsize=(10,10))
sns.heatmap(corr,cmap = 'coolwarm' ,annot = True)
plt.show()

ip = data.drop(['Y1','Y2','X6','X8'],axis=1)
op1 = data['Y1']
op2 = data['Y2']

from sklearn.model_selection import train_test_split

x_train , x_test , y_train1 , y_test1 = train_test_split(ip,op1,test_size=0.2)


from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(x_train,y_train1)


print(model.score(x_test,y_test1))

x_train , x_test , y_train2 , y_test2 = train_test_split(ip,op1,test_size=0.2)

model1 = LinearRegression()
model1.fit(x_train,y_train2)


print(model1.score(x_test,y_test2))



