# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 15:20:19 2019

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt
n_pts = 200
x = np.linspace(0,10,n_pts)
y = 5*x+14
y = 5*x+14 + np.random.uniform(-5,5,n_pts)

plt.scatter(x,y,color='b')
plt.show() 

from sklearn.linear_model import LinearRegression
# sklearn package ->package for machine learning
# linear_model -> submodel , LinearRegression -> Class , by convention we keep class as capital 
# If the data contains a single feature/single input reshape to (-1,1)
# If the data contains a single sample reshape to (1,-1)
# else it gives error

model = LinearRegression()
model.fit(x.reshape(-1,1),y)

# to predict the line

plt.figure(figsize=(10,10))
plt.scatter(x,y,color = 'b')
plt.plot(x,model.predict(x.reshape(-1,1)),color='r')
plt.show()

# to show the point
un = np.array([2.75])
model.predict(un.reshape(1,-1))
plt.scatter(un,model.predict(un.reshape(1,-1)),color='g')
plt.show()

#
plt.figure(figsize=(10,10))
plt.scatter(x,y,color = 'b')
plt.plot(x,model.predict(x.reshape(-1,1)),color='r')
plt.scatter(un,model.predict(un.reshape(1,-1)),color='g')
plt.show()