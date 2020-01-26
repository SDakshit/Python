# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 20:44:58 2019

@author: hp
"""

def fibo(n):
    if n==0:
        return 0
    elif (n==1 or n==2):
        return 1
    else:
        return(fibo(n-1)+fibo(n-2))
        
n=int(input("enter no of terms"))
l=[]
for i in range(0,n):
    l.append(fibo(i))
    
s=0
for i in range(0,len(l)):
    if((i+1)%2==0):
        s+=l[i]
print(l)
print("sum of even values terms=",s)