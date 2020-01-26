
n=int(input("enter the no. of element"))
a=[]
for i in range(0,n):
    y=input("enter the elements")

    a.append(y)
 

a.sort()
print("\n the sorted list is-",a)
x=int(input("enter the element to be searched"))
for i in range (n):
    if(i==x):
        print("\n element found at",i,"position")
        break
a.remove(i)
print("\n the final array is-",a)