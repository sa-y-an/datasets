# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 14:18:56 2020

@author: user
"""


import numpy as np
from sklearn.preprocessing import MinMaxScaler

data = np.random.randint(0,100,(10,2))

scaler_module = MinMaxScaler()

data1 = scaler_module.fit_transform(data)


x_train , x_test , y_train , y_test 