# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 16:15:27 2019

@author: user
"""

import numpy as np
import matplotlib.pyplot  as plt
from sklearn.datasets import load_diabetes

data = load_diabetes()
ip = data.data[:,np.newaxis,2]
op = data.target

plt.scatter(ip,op)
plt.show()

# linearRegression 
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression
model = LinearRegression()

x_train , x_test , y_train , y_test = train_test_split(ip,op,test_size=0.2)

#model = LinearRegression()

model.fit(x_train,y_train)
plt.scatter(ip,op)

#plt.plot(x_test,model.predict(x_test),color='r')
#plt.plot(x_train,model.predict(x_train),color='y')
plt.plot(ip,model.predict(ip),color='y')


print(model.score(x_test,y_test))