# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 20:33:23 2019

@author: hp
"""

try:
    l=[]
    print("enter a list:")
    while True:
        l.append(int(input()))
except:
    n=int(input("enter a number "))
    t=[]
    count=0
    for i in range(0,len(l)):
        if l[i]==n:
            count+=1
            t.append(i)
    print("frequency of",n,"is",count)
    print("indeces are ",t)
    1