# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 13:54:58 2019

@author: user
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv(r"D:\Datasets\Churn_Modelling.csv") 

#count plot using seaborn
sns.countplot(data.Gender)
plt.show()

# to find no of people leaving the bank
sns.countplot(data.Gender[data.Exited == 1])
plt.show()

sns.countplot(data.Geography[data.Exited == 1])
plt.show()

# distribution plot (plotting a histogram)

plt.figure(figsize = (10,10))
sns.distplot(data.CreditScore[data.Exited == 0 ])
#plt.show() 
#plt.figure(figsize = (10,10))
sns.distplot(data.CreditScore[data.Exited == 1 ])

plt.legend(['not_exited','exited'])
plt.show()


 # age 
 
 
plt.figure(figsize = (10,10))
sns.distplot(data.Age[data.Exited == 0 ])
#plt.show() 
#plt.figure(figsize = (10,10))
sns.distplot(data.Age[data.Exited == 1 ])

plt.legend(['not_exited','exited'])
plt.show() 


# Heat Map

# corr(x,y) = cov(x,y)/std(x)*std(y)
# corr = 0 -> no relation
#      = 1 -> direct
#      = 1 -> inverse

corr = data.corr()
# correlation in have_Credit is dependent on rank

plt.figure(figsize=(20,10))
sns.heatmap(corr,cmap='rainbow',annot = True)
plt.show()

# it causes problems in boolean data since it starts ranking it (1>0) but we cant
# not say (yes>no) 

# Pair Plot
# PLOTS everything

sns.pairplot(data)
plt.show() 

# Swarm plot 
# it is used to predict the best efficiency among them

plt.figure(figsize=(10,10))
data2 = pd.read_csv(r"D:\Datasets\maintenance_data.csv")

sns.swarmplot(data2.team,data2.lifetime, hue = data2.broken )
plt.show()


plt.figure(figsize=(10,10))
sns.swarmplot(data2.provider,data2.lifetime, hue = data2.broken )
plt.show()






