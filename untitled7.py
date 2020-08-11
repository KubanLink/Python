#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 18:25:40 2020

@author: corbinyoung
"""
def EVn():
    S=[1,2,3,4,5,6,7,8,9]
    N=[]
    for x in S:
        x%2
        if x%2==0:
            N.append(x)
            print(N)
            
EVn()
#---------------------------
def Even():
    S=[1,2,3,4,5,6,7]
    N=[]
    for x in S:
        x%2+1
        if x%2+1==True:
            N.append(x)
            print(x)
            
Even()

'''def Palin():
    x=input('test word is palindrome')
    x.reverse(x)
    if x==True:
        print(x)
Palin()'''