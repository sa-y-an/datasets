# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 14:53:52 2019

@author: user
"""


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv(r"D:\Datasets\maintenance_data.csv")
ip = data.drop(['broken'],axis=1)
op = data['broken']

from sklearn.preprocessing import LabelEncoder


le1 = LabelEncoder()
ip.team = le1.fit_transform(ip.team)

le2 = LabelEncoder()
ip.provider = le2.fit_transform(ip.provider)


from sklearn.preprocessing import OneHotEncoder

ohe = OneHotEncoder(categorical_features=[4,5])
ip = ohe.fit_transform(ip).toarray()



from sklearn.model_selection import train_test_split
xtr,xts,ytr,yts = train_test_split(ip,op,test_size=0.2)


from sklearn.preprocessing import StandardScaler
sc = StandardScaler() 
sc.fit(xtr) 
xtr = sc.transform(xtr)
xts = sc.transform(xts)


from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(xtr,ytr)


from sklearn.metrics import confusion_matrix
y_pred = model.predict(xts)
print(confusion_matrix(yts,y_pred))




