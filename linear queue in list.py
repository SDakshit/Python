# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 15:28:39 2019

@author: Student
"""

queue=[]

front=-1
rear=-1

def enque(n):
    global queue
    global front
    global rear
    
    if rear==-1 and front==-1:
        rear=0
        front=0
    else:
        rear=rear+1
    
    queue.append(n)
    
def deque():
    global front
    global rear
    
    if front>rear:
        print('UNDERFLOW')
        return
    
    front=front+1
    
while True:
    print('-------MAIN MENU--------')
    print('1.Enque')
    print('2.Deque')
    print('3.Display')
    print('4.Exit')
    n=int(input('Enter Choice: '))

    if(n==1):
        p=int(input('Enter element: '))
        enque(p)
    elif n==2:
        deque()
    elif n==3:
        for i in range(front,rear+1):
            print(queue[i])
    else:
        break
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        