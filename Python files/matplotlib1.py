# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 09:19:33 2019

@author: user
"""

import matplotlib.pyplot as plt
import numpy as np

# Curves

x = [1,2,3,4,5,6]
y = [3,6,8,5,10,10]

# maintain same x and y

plt.plot(x,y,color='red',linewidth='5')

plt.title('Title')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.show()

#legends

x1 = np.linspace(0,10,10)
y1 = 5*x1+12
y2 = 7*x1+12

plt.title('Label')
plt.xlabel('x axis')
plt.ylabel('y axis')


plt.plot(x1,y1,color = 'r',label='l1')
plt.plot(x1,y2,color = 'b',label='l2')
plt.legend()
plt.show()

# Quadratic Functions

x2 = np.linspace(-10,10,100)
y3 = x2**2


plt.figure(figsize=(10,10))
plt.plot(x2,y3,color='cyan',linewidth=5)  
plt.xlim(0,8)  #sets limits on x axis (from __ to ___)
plt.xticks(np.arange(-8,8,2),rotation = 90)  #to change spaces b/w x coordinates 
#plt.grid(color='b')
#to change grid lines
plt.grid(color='b',ls='-.',lw = 2)
#lw showes thickness
# ls changes it to broken line

plt.show()

# Bar Graphs


x = ['Kohli','Rohit','Raina','Sakib']
y = [1,0,5,3]
plt.bar(x,y,color='magenta')
plt.show()

plt.bar([1,2,3,5,7,8],[8,9,3,4,6,7],color='c' , label = 'eg1')
plt.bar([2,4,6,8,10,7],[9,5,4,6,7,2],color='m' , label = 'eg2')


# Histogram

age = np.random.randint(1,50,30)
bins = np.arange(0,50,10)
plt.hist(age,bins,rwidth=0.97) #rwidth gap between rows
plt.show()

# scatter
'''
. A scatter plot is a type of plot that shows the data as a collection of points.
 The position of a point depends on its two-dimensional value,
 where each value is a position on either the horizontal or vertical dimension.
 '''
 
x = np.random.normal(10,2,100)
y = np.random.normal(10,2,100)

plt.scatter(x,y,color='y')
plt.show()

# Area Plot

days = [1,2,3,4,5,6,7,8]
visitors = np.random.randint(100,1000,8)
re_visitor = np.random.randint(0,500,8)

plt.plot([],[],color = 'm' ,label = 're_visitor')
plt.plot([],[],color = 'b' ,label = 'visitors')


# dummy pplots to show labels


plt.stackplot(days,re_visitor,visitors,colors = ['m','c'])
plt.legend()
plt.show()

# pie chart

activities = ['work','exercise','sleep','eat','PUBG']
slices = [8,1,8,3,4]
plt.pie(slices,labels=activities,colors=['pink','orange','blue','violet','cyan'],explode=[0,0.5,0,0,0],shadow=True)
plt.show()


# contour plot

xlist = np.linspace(-3,3,100)
ylist = np.linspace(-3,3,100)

xx,yy = np.meshgrid(xlist,ylist)

z = np.sqrt(xx**2+yy**2)

plt.contourf(xx,yy,z)
plt.show()

# Box plot 
# used to normalize the data (to change the scale of the data withou affecting it)

a1 = np.random.normal(100,10,200)
a2 = np.random.normal(80,30,200)
a3 = np.random.normal(90,20,200)
a4 = np.random.normal(70,25,200)
data = [a1,a2,a3,a4]
plt.boxplot(data)
plt.show()

plt.violinplot(data)
plt.show()


# 3D-plots

from mpl_toolkits import mplot3d

fig = plt.figure()
ax = plt.axes(projection='3d')
z= np.linspace(0,1,100)
x = z*np.sin(z)
y = z*np.cos(z)
ax.plot3D(x,y,z,'g')
plt.show()



fig = plt.figure()  # area for figure
ax = plt.axes(projection='3d') # creates axes
t = np.linspace(0,1,100)
x = 2*t**2
y = 4*t
ax.plot3D(x,y,z,'g')
plt.show()



# 3D wireframe


def f(x,y):
    return np.sin(np.sqrt(x**2+y**2))

x = np.linspace(-6,6,30)
y = np.linspace(-6,6,30)

X,Y = np.meshgrid(x,y) # it creates a grid from where function values are plotted (by their height )
z= f(X,Y)
fig = plt.figure()
ax =plt.axes(projection='3d')    
ax.plot_wireframe(X,Y,z,color='g')
ax.set_title('wireframe')
#to add a surface

ax.plot_surface(X,Y,z,cmap='rainbow') # cmap gives color map (eg rainbow , winter )
plt.show()





# more than one plot // Subplots


fig , axes = plt.subplots(nrows=2,ncols=2) # creates 4 plots

axes[0][0].plot([1,2,3],[1,2,3]) # this way we add graphs in plots using array indices
plot.show()


