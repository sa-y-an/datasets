# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 15:42:59 2019

@author: user
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv(r"D:\Datasets\auto-mpg.csv" , header = None )
data.columns = ['mpg','cylinders','displacement','horsepower','weight','acceleration','model_year','origin','car_name']

for i in ['horsepower'] :
    data[i].replace('?',  data.describe(include='all')[i][2],inplace = True)
    
for i in ['horsepower'] :
    print(sum(data[i]=='?'))
    
data['horsepower'] = data.horsepower.astype(float)

ip = data.drop(['mpg','car_name'],axis = 1) # INPUT VARIABLE
#ip.head(2)
op = data['mpg']  # OUTPUT VARIABLE
#ip.head()

from sklearn.model_selection import train_test_split
# tts is a method
# it returns 4 values 
# x_train , x_test , y_train , y_test

x_train , x_test , y_train , y_test = train_test_split(ip,op,test_size=0.2)
# x_train , y_train -> uses data for training
# x_test , y_test -> uses data for testing
# 

from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(x_train,y_train)

model.score(x_test,y_test)


# mse , mae , rme

