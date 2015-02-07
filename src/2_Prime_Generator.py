'''
Created on Sep 13, 2014

@author: Shathru
'''
"""
The input begins with the number t of test cases in a single line (t<=10).
In each of the next t lines there are two numbers m and n (1 <= m <= n <= 1000000000, n-m<=100000) separated by a space.
"""

#Generate the prime numbers in the given range of numbers
def prime(start, end):
    prm_lst = [];
    for num in range(int(start),int(end)+1):
        prime = True
        if(num==2):
            prime = True
        if(num >2 and num%2==0):
            prime = False
        if(num==1):
            prime = False
        for i in range(3,int(num/2)):
            if (num%i==0):
                prime = False
        if prime:
            prm_lst.append(num)
    return prm_lst;

t = input()
num = []
new_lst = []

for i in range(0,int(t)):
    a = input();
    num.append(a.split());    

for i in range(0,len(num)):
    new_lst.append(prime(num[i][0],num[i][1]))
    
""" Printing the prime numbers """
for i in range(0,len(new_lst)):
    for j in range(0,len(new_lst[i])):
        print (new_lst[i][j])
    print("\n")