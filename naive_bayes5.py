# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 15:25:09 2019

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
a = iris.DESCR

ip = iris.data[ :,2 : 4]
op = iris.target

plt.scatter(ip[:,0],ip[:,1],c=op)
plt.show()


from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(ip,op)


x_max , x_min = ip[:,0].max(), ip[:,0].min()
y_max , y_min = ip[:,1].max(),ip[:,1].min()

xx , yy = np.meshgrid(np.linspace(x_min,x_max),np.linspace(y_min,y_max))
grid = np.c_[xx.ravel(),yy.ravel()]
pred = model.predict(grid).reshape(xx.shape)
plt.contourf(xx,yy,pred)
plt.scatter(ip[:,0],ip[:,1],c=op)
plt.show()

from sklearn.naive_bayes import GaussianNB

modelNB = GaussianNB()
modelNB.fit(ip,op)

predNB = modelNB.predict(grid).reshape(xx.shape)


x_max , x_min = ip[:,0].max(), ip[:,0].min()
y_max , y_min = ip[:,1].max(),ip[:,1].min()

xx , yy = np.meshgrid(np.linspace(x_min,x_max),np.linspace(y_min,y_max))
grid = np.c_[xx.ravel(),yy.ravel()]
pred = modelNB.predict(grid).reshape(xx.shape)
plt.contourf(xx,yy,pred)
plt.scatter(ip[:,0],ip[:,1],c=op)
plt.show()

from sklearn.svm import SVC
modelSV = SVC(kernel = 'poly', C = 1000 , gamma = 0.1)
modelSV.fit(ip,op)

predSV = modelSV.predict(grid).reshape(xx.shape)

plt.contourf(xx,yy,predSV)
plt.scatter(ip[:,0],ip[:,1],c=op)
plt.title('SVC')
plt.show()

from sklearn.svm import SVC
modelSV = SVC(kernel = 'linear', C = 1000 , gamma = 0.1)
modelSV.fit(ip,op)

predSV = modelSV.predict(grid).reshape(xx.shape)

plt.contourf(xx,yy,predSV)
plt.scatter(ip[:,0],ip[:,1],c=op)
plt.title('SVC')
plt.show()


from sklearn.svm import SVC
modelSV = SVC(kernel = 'rbf', C = 1000 , gamma = 0.1)
modelSV.fit(ip,op)

predSV = modelSV.predict(grid).reshape(xx.shape)

plt.contourf(xx,yy,predSV)
plt.scatter(ip[:,0],ip[:,1],c=op)
plt.title('SVC')
plt.show()

