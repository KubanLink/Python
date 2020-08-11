#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 14:58:42 2020

@author: corbinyoung
"""

'Import matplotlib'
import matplotlib.pyplot as plt

'Import numbpy'
import numpy as np

'create an outline shape'
r=-1
q= -0.5
t=np.linspace(0,2*np.pi,1000)
d=np.linspace(0,2*np.pi,1000)
'create pupils'
e=0.5
e1=0.0
e2=-0.5
e3=0.0

'create eyeballs'
EB=0.5
E1=0.0
E2=-0.5
E3=0.0

'create circles around pupils'
w=0.0,-0.75
p=np.linspace(0,2*np.pi,100)


'Circle using Trignometry'
x=r*np.cos(t)
y=r*np.sin(t)
plt.scatter(x,y,c='red',s=50)

'Yellow outline'
x2=r*np.cos(d)
y2=r*np.sin(d)
plt.scatter(x2,y2,c='yellow',s=30)

'Pupil 1'
plt.scatter(e,e1,c='red', s=5000)

'Pupil 2'
plt.scatter(e2,e3, c='red', s=5000)

'Eye Balls'
plt.scatter(EB,E1,c='orange',edgecolors='black',s=900)
plt.scatter(E2,E3,c='orange',edgecolors='black',s=900)

'Goggles'
pp=r*np.cos(p)
p2=r**q*np.sin(p)
# I create a straight line to find the lenght for my circle
haha=np.linspace(0.5,-0.5)
ahah=np.linspace(-0.5,-0.5)

#Goggles
plt.scatter(pp,p2,c='orange',s=50)
#Bottom Lip
plt.scatter(haha, ahah, c='orange',s=100)

'Nose w/ Sunblock'
n=0.0
n1=-0.25
plt.scatter(n,n1,edgecolor='r',lw=2,c='w',s=700,marker='8')

#Uppeer Lip
xz=np.linspace(-0.60,0.60)
zx=np.linspace(-0.5,-0.5)
hat=np.sin(zx)
tah=np.cos(xz)
plt.scatter(xz,hat,c='r')







