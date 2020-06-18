# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 14:52:20 2019

@author: user
"""

import pandas as pd

#the r before file path ensures \ is not read as escape character
# nad -> refers null values 
# what to fill in nad depends on the data
# mostly we replace by top trnding values 

data = pd.read_csv(r"D:\Datasets\movie_metadata.csv")
# this creates a memory instance where the data is stored 

null = data.isnull()
w1 = data.isnull().sum() #tells column wise

w2 = data.isnull().sum().sum() # tells entirely

# remove nulls 

#data1 = data.dropna(axis=0)  # remove rows

#data2 = data.dropna(axis=0, inplace= True) #drops null value

#data.fillna('X',inplace = True) # inplacing inplace = True replaces in the original data set instead of giving output as data  
# to reflect live updates we need connect through web_hook through API's

# data descriptions

data.mean() # each column
data.std() # standard devuiation

desc = data.describe() #every thing at only numeric columns
desc1 = data.describe(include="all") #every thing including string columns

data.fillna(data.mean(),inplace = True)

#data.fillna(data.mean(),inplace = True)


data['color'].dtype #find types

data.columns #returns column names

data.fillna('x',inplace=True)

for i in data.columns :
    if data[i].dtype  == 'O' :
        data[i].replace('x',data.describe(include = 'all')[i][2],inplace=True)
    

# When no header is present
        
        
data2 = pd.read_csv(r"D:\Datasets\auto-mpg.csv",header=None) 
#to specify the column names

data2.columns = ['mpg','cyllinder','displacement','horsepower','weiight','accel','model_year','origin','car_name']

data.fillna('x',inplace=True)

for i in data2.columns :
    if data2[i].dtype  == 'O' :
        data2[i].replace('?',data2.describe(include = 'all')[i][2],inplace=True)

data2['horsepower'].replace('?',data2.describe(include='all')['horsepower'][2],inplace=True  )      
data2['horsepower']= data2['horsepower'].astype(float)  

#Data Frames

dic = {'day':[1,2,3,4,5,6],'visitors':[100,200,75,60,65,35]}

data3 = pd.DataFrame(dic) 

data3.to_csv(r"D:\Datasets\data3.csv")
data3.to_excel(r"D:\Datasets\data34.xlsx")











