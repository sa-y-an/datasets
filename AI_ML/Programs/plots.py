# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 09:12:27 2019

@author: shamaun
"""

import matplotlib.pyplot as plt
import numpy as np

#curve

x = [1,2,3,4,5,6]
y = [3,6,8,5,10,10]

plt.plot(x,y,color='red',linewidth=5)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Title')
plt.show()


x1 = np.linspace(0,10,10)
y1 = 5*x1 + 12
y2 = 7*x1 + 14

plt.plot(x1,y1,color='r',label='line 1')
plt.plot(x1,y2,color='b',label='line 2')
plt.legend()
plt.show()

x2 = np.linspace(-10,10,100)
y3 = x2**2
plt.figure(figsize=(10,10))
plt.plot(x2,y3,color='r')
plt.xlim(-8,8)
plt.ylim(0,80)
plt.xticks(np.arange(-8,8,1),
           rotation = 90)
plt.grid(color='b',ls='-.',lw=2)
plt.show()

#bar graph

x = ['Kohli','Rohit','Raina','Shakib']
y = [120,90,75,100]

plt.bar(x,y,color='m')
plt.show()


plt.bar([1,3,5,7,9],[8,9,3,4,6],
        color='c',label= 'eg 1')
plt.bar([2,4,6,8,10],[9,5,6,4,7],
        color='m',label= 'eg 2')
plt.legend()
plt.show()


#histogram

age = np.random.randint(1,50,30)
bins = np.arange(0,50,10)

plt.hist(age,bins,rwidth=0.97,color='g')
plt.show()


#scatter

x = np.random.normal(10,2,100)
y = np.random.normal(10,2,100)
plt.scatter(x,y,color='r')
plt.show()


#area
days = [1,2,3,4,5,6,7,8]
visitors = np.random.randint(100,1000,8)
re_visitors = np.random.randint(0,500,8)
plt.plot([],[],color='m',label='re_visitors')
plt.plot([],[],color='c',label='visitors')
plt.stackplot(days,re_visitors,visitors,
              colors=['m','c'])
plt.legend()
plt.show()


#pie chart

activities = ['work',
              'exercise',
              'sleep',
              'eat',
              'PUBG']
slices = [8,1,8,3,4]
plt.pie(slices,labels=activities,
        colors=['r','g','b','c','m'],
        explode=[0,0.5,0,0,0],
        shadow=True)
plt.show()

#contour plot

xlist = np.linspace(-3,3,100)
ylist = np.linspace(-3,3,100)
xx,yy = np.meshgrid(xlist,ylist)
z = np.sqrt(xx**2+yy**2)
plt.contourf(xx,yy,z)
plt.show()


#box plot

a1 = np.random.normal(100,10,200)
a2 = np.random.normal(80,30,200)
a3 = np.random.normal(90,20,200)
a4 = np.random.normal(70,25,200)
data = [a1,a2,a3,a4]
plt.boxplot(data)
plt.show()

plt.violinplot(data)
plt.show()


#3D-plots

from mpl_toolkits import mplot3d

fig = plt.figure()
ax = plt.axes(projection='3d')
z = np.linspace(0,1,100)
x = z*np.sin(z)
y = z*np.cos(z)
ax.plot3D(x,y,z,'g')
plt.show()


#3D wireframe

def f(x,y):
    return np.sin(np.sqrt(x**2+y**2))

x = np.linspace(-6,6,30)
y = np.linspace(-6,6,30)

X,Y = np.meshgrid(x,y)
z = f(X,Y)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_wireframe(X,Y,z,color='g')

ax.plot_surface(X,Y,z,cmap='rainbow')
plt.show()






fig, axes = plt.subplots(nrows=2,
                         ncols=2)

axes[1][0].plot([1,2,3],[1,2,3])
plt.show()

























