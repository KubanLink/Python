#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 14 18:05:40 2020

@author: corbinyoung
"""

#User Input; 2(Strings),2(Numbers),(Number+String)
def supertime():
    x=input()
    noW1=x.strip()
    y=input()
    noW2=y.strip()    
    #Bool Input1
    A=noW1.isalpha()    #IS X==LETRR
    #Bool Input2
    L=noW2.isalpha()    #IS Y==LETRR
    #IF A=1 or True 
    if A>0:   
        A1=x.upper()
    else:
        num1=int(x)
        N1=(num1*num1)
    #IF L=1 or True 
    if L>0:
        A2=y.upper()
    else:
        num2=int(y)
        N2=(num2*num2)
    #Outputs...Concatenation||Multiplication of Squares
    if A>0 and L>0:
        print(A1+" "+A2)
    else:
        print(N1*N2)

supertime()
supertime()
supertime()