# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 23:50:47 2019

@author: user
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel(r"C:\Users\user\Downloads\RESULT_OF_B_TECH_B.TECH_AND_M_TECH_DUAL_DEGREE_INTEGRATE_zqSbrM7.xlsx")
data2 = data.drop(['Index'],axis=1)

data.columns 

data7 = data.Program

data8 = data[data.Program == 'B.Tech-EE']

data8.Program.count()

data['Program'].dtype

for i in data8.columns :
    if data8[i].dtype == 'O' :
        data8[i].replace('nan',  0,inplace = True)
