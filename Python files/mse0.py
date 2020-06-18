# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 09:23:05 2019

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

n_pts = 100
x = np.linspace(0,10,n_pts)

y = 5*x+14 + np.random.uniform(-5,5,n_pts)
model = LinearRegression()
model.fit(x.reshape(-1,1),y)

m = model.coef_
c = model.intercept_

x1= 0.5
y1 = m*x1 + c
x2 = 10
y2 = m*x2 + c

plt.scatter(x,y)
plt.plot([x1,x2],[y1,y2],c='r',lw = 5)

y_pred = model.predict(x.reshape(-1,1))
mse = (np.subtract(y_pred,y)**2).sum()/100
print(mse)

r2score = model.score(x.reshape(-1,1),y)
print(r2score)
