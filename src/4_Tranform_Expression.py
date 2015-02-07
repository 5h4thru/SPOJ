'''
Created on Sep 13, 2014

@author: Shathru
'''
"""
Transform the algebraic expression with brackets into RPN form (Reverse Polish Notation).
Two-argument operators: +, -, *, /, ^ (priority from the lowest to the highest), brackets ( ).
Operands: only letters: a,b,...,z. Assume that there is only one RPN form (no expressions like a*b*c).
"""

t = input()
a,b,c = [],[],[]
exp = {
       "^":1,
       "/":2,
       "*":3,
       "-":4,
       "+":5
       }

for i in range(0,int(t)):
    a.append(input())
print (a)
for i in range(0,len(a)):
    for j in range(0,len(a[i])):
        if not(a[i][j]=="(" or a[i][j]==")"):
            b.append(a[i][j])

for i in b:
    if i not in exp:
        print (i),
    else:
        if len(c)==0:
            c.append(i)
        else:
            for j in range (0,len(c)):
                if (exp[i] > exp[c[j]]):
                    c.append(i)
                else:
                    print (i)