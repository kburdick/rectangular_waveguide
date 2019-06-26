# -*- coding: utf-8 -*-
"""
Purpose: Visualizing TM (Transverse Magnetic) modes in a rectangular waveguide
Author: Kurt Burdick
created: 3/6/2019
date modified: 6/26/19
"""
import numpy as np
import matplotlib.pyplot as plt

#import matplotlib.cm as cm
#B_z = 0 b/c transverse magnetic modes
#want to plot E^2, this will get you the intensity of the E-Field

#define constants and waveguide size
E0 = 100
a = 6
b = 1
m = 1
n = 1
pi = np.pi

#define grid 
x = np.linspace(0,6,6000)
y = np.linspace(0,1,1000)
x, y = np.meshgrid(x, y)

#make field equations
E_x = -100*(m*pi/a)*np.cos(m*pi*x/a)*np.sin(n*pi*y/b)
    
E_y = -100*(n*pi/b)*np.sin(m*pi*x/a)*np.cos(n*pi*y/b)

E_z = 100*(np.sin(m*pi*x/a)*np.sin(n*pi*y/b))
    
E_1 = (E_x*E_x + E_y*E_y + E_z*E_z)
    
E = np.sqrt(E_1)
        
#Adjust figures  
fig = plt.figure()
ax = fig.add_subplot(111)

#make contour plot with mapping colors
cpf = ax.contourf(x,y,E_1, 20, cmap='coolwarm_r')
plt.xlabel('a')
plt.ylabel('b')
plt.title('Transverse Magnetic modes in a Rectangular Waveguide')
plt.show()