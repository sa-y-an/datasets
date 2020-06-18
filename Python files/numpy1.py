# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 16:41:08 2019

@author: user
"""
import numpy as np

arr1=np.random.randint(1,10,(3,4))
arr2=np.random.randint(1,10,(3,4))

# Array Manipulation

#Reshaping arrays
res=arr2.reshape(6,2)#or 2,6 or 4,3 or 3,4 

#Concatenation
con=np.concatenate((arr1,arr2),axis=0)# axis=0 => row
                                      # axis=1 => column

#Append
apnd =np.append(arr2,[1,2,3,4]) # Flattens the array and adds elements at the end

#Insert
insrt=np.insert(arr1,2,[1,2,3,4]) # Flattens the array and inserts elements at given index

#Flattening the array
flat=arr1.ravel()
flat2=arr1.flatten()

#Alternate concatenation
conc2=np.c_[arr1,arr2]

#Getting stats of the array

np.mean(arr1)
np.std(arr1)
np.median(arr1)
np.var(arr1)

#Scalar operations on arrays

add=np.add(arr1,2)
sub=np.subtract(arr1,2)
div=np.divide(arr1,2)
mul=np.multiply(arr2,3)
exp=np.power(arr2,2)

#Vector operations on arrays

vadd=np.add(arr1,arr2)
vsub=np.subtract(arr1,arr2)
vdiv=np.divide(arr1,arr2)
vmul=np.multiply(arr2,arr1)
vexp=np.power(arr1,arr2)

#Garbage value exception/Insufficient bit/variable size

a=np.array([[1,2,3],[4,5,6]])
b=np.array([[7,8,9],[10,10,10]])
c=np.power(np.int64(a),np.int64(b))

