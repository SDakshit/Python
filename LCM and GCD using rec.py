def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
a=int(input("enter the 1st number"))
b=int(input("enter the 2nd number"))
GCD=gcd(a,b)
lcm=(a*b)/GCD
print("GCD=",GCD)
print("LCM=",lcm)