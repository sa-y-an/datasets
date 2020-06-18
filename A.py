# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np

a=np.array([1,2,3])
a2=np.array([[1,2,3],[4,5,6]])

zeros=np.zeros((2,4))
z_l=np.zeros_like(a2)

ones=np.ones((3,3))
o_l=np.ones_like(a2)

full=np.full((3,3),5) #3x3 filled with 5s
f_l=np.full_like(a2,13)

identity= np.eye(5)
trans=a2.T

lins=np.linspace(0,100,5) # linear distribution according to no of parts
arange=np.arange(0,10,3)  # linear distribution according to step value

# 3x4 array of random floats
# between 0 and 100 
rand=np.random.rand(3,4)*100

#3x4 array of random integers between 10 and 50
randint=np.random.randint(10,50,(3,4))

#normal data distribution
normal=np.random.normal(10,2,10) 

#uniform data distribution

uniform = np.random.uniform(-5,5,100)
np.random.uniform()

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
b=np.array([[7,8,9],[10,11,12]])

c=np.power(np.int64(a),np.int64(b))





