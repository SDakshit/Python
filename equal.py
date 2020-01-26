def equal(a,b):
    if(a==b):
        return 1
    else:
        return 0
a=int(input("enter the 1st number"))
b=int(input("enter the 2nd number"))
r=equal(a,b)
if(r==1):
    print("equal")
else:
    print("not equal")