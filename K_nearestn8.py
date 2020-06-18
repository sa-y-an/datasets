# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 12:13:26 2019

@author: user
"""
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
import numpy as np
import matplotlib.pyplot as plt


from sklearn.datasets import load_wine
wine = load_wine()

features = wine.data[:, :2]
labels = wine.target
# plt.scatter(features,labels)


modelLR = LogisticRegression()
modelNB = GaussianNB()
modelSV = SVC(kernel='poly', C=100, gamma=1)
modelKNN = KNeighborsClassifier(n_neighbors=14)


modelLR.fit(features, labels)
modelNB.fit(features, labels)
modelSV.fit(features, labels)
modelKNN.fit(features, labels)


x_max, x_min = features[:, 0].max()+1, features[:, 0].min()-1
y_max, y_min = features[:, 1].max()+1, features[:, 1].min()-1

xx, yy = np.meshgrid(np.linspace(x_min, x_max), np.linspace(y_min, y_max))
grid = np.c_[xx.ravel(), yy.ravel()]
predLR = modelLR.predict(grid).reshape(xx.shape)
predNB = modelNB.predict(grid).reshape(xx.shape)
predSV = modelSV.predict(grid).reshape(xx.shape)
predKNN = modelKNN.predict(grid).reshape(xx.shape)

fig, axes = plt.subplots(nrows=4, ncols=1, squeeze=False, figsize=(5, 10))
fig.tight_layout()

axes[0][0].contourf(xx, yy, predLR)
axes[0][0].scatter(features[:, 0], features[:, 1], c=labels)


axes[1][0].contourf(xx, yy, predNB)
axes[1][0].scatter(features[:, 0], features[:, 1], c=labels)


axes[2][0].contourf(xx, yy, predSV)
axes[2][0].scatter(features[:, 0], features[:, 1], c=labels)

axes[3][0].contourf(xx, yy, predKNN)
axes[3][0].scatter(features[:, 0], features[:, 1], c=labels)

