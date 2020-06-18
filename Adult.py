# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 09:18:13 2019

@author: user
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#delimiter = removes white spaces
data = pd.read_csv(r"C:\Users\user\Downloads\adult.data" , header = None , delimiter =' *, *',engine = 'python')
data.columns = ['age','workclass','fnlwgt','education','education_num','marital_status','occupation','relationship','race','sex','capital_gain','capital_loss','hours_per_week','native_country','income']

#fnlwgt in this data represents no.  of people in this data_set 

for i in data.columns :
    if data[i].dtype == 'O' :
        print(i,':',sum(data[i]=='?'))


desc = data.describe(include = 'all')

for i in data.columns :
    if data[i].dtype == 'O' :
        data[i].replace('?',  data.describe(include='all')[i][2],inplace = True)



from sklearn.preprocessing import LabelEncoder

le1 = LabelEncoder()
data.workclass = le1.fit_transform(data.workclass)
le2 = LabelEncoder()
data.education = le2.fit_transform(data.education)
le3 = LabelEncoder()
data.marital_status = le3.fit_transform(data.marital_status)
le4 = LabelEncoder()
data.occupation = le4.fit_transform(data.occupation)
le5 = LabelEncoder()
data.occupation = le5.fit_transform(data.occupation)
le6 = LabelEncoder()
data.relationship = le6.fit_transform(data.relationship)
le7 = LabelEncoder()
data.race = le7.fit_transform(data.race)
le8 = LabelEncoder()
data.sex = le8.fit_transform(data.sex)
le9 = LabelEncoder()
data.native_country = le1.fit_transform(data.native_country)


# OneHotEncode

ip = data.drop(['income'],axis=1)
op = data.income

from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(categorical_features = [1,3,5,6,7,8,9,13])
ip = ohe.fit_transform(ip).toarray()


from sklearn.model_selection import train_test_split

xtr,xts,ytr,yts = train_test_split(ip,op,test_size=0.2)


from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
sc.fit(xtr)

xtr = sc.fit_transform(xtr)
xts = sc.fit_transform(xts)

from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(xtr,ytr)

from sklearn.metrics import confusion_matrix
y_pred = model.predict(xts)

print(confusion_matrix(yts,y_pred))

model.score(xts,yts)

# plotting distribution of age of income == >=50k
''''
age_hi = data.age[data.income=='>50K']
age_low = data.age[data.income=='<50k']
bins = np.arange(10,100,10)
plt.hist([age_hi,age_low],bins)
'''


'''
corr = data.corr()
plt.figure()

ip = data.drop['income']
op = data['income']
'''

        