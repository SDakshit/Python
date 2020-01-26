# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 22:07:55 2019

@author: hp
"""

list1=["Naruto","Sasuke","Kakashi","Hinata","Gara"]
list2=[12,13,11,14,10]
tallest=max(list2)
name=list2.index(tallest)
print("Tallest friend is ",list1[name],"with height= ",tallest)
shortest=min(list2)
name=list2.index(shortest)
print("Shortest friend is ",list1[name],"with height= ",shortest)
mean=sum(list2)/5
m=list2.index(mean)
print("Mean friend is  ",list1[m], "with height= ",m)