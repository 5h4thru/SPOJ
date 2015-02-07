'''
Created on Sep 13, 2014

@author: Shathru
'''

def isPrime(x):
    p = True
    if x==1:
        p = False
    if x==2:
        p = True
    for i in range(2,int(x**0.5)+1):
        if x>2 and x%i==0:
            p = False
    return p
         
# getting inputs here
t=input()
n,m=[],[]
for i in range (0,int(t)):
    a,b=input().split()
    n.append(int(a))
    m.append(int(b))

# printing prime numbers in t(th) case
for i in range (0,int(t)):
    for j in range (n[i],m[i]+1):
        if isPrime(j): print (j)
    print ()