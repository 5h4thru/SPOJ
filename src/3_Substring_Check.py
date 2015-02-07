'''
Created on Sep 13, 2014

@author: Shathru
'''
"""
Given two binary strings, A (of length 10) and B (of length 5), output 1 if B is a substring of A and 0 otherwise.
"""
n=[]
for i in range (0,3):
    a = input()
    n.append(a.split())

def isPresent(a,b):
    if b in a:
        print(1)
    else:
        print(0)

for i in range (0,len(n)):
    if(n[i][1] in n[i][0]): print(1)
    else: print(0)