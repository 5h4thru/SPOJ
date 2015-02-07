'''
Created on Sep 15, 2014

@author: Shathru
'''
def isPalindrome(a):
    res = 0
    given = a
    while (a != 0):
        b = a % 10
        a = int(a / 10) #Can use (a // 10)
        res = (res * 10) + b
    if given == res:
        return True
    else:
        return False

k = input()
result = []
for i in range(0,int(k)):
    num = input()        
    next_num = int(num)
    if (num == num[::-1]):
        next_num += 1
    while (not isPalindrome(next_num)):
        next_num += 1
    result.append(next_num)

for i in result:
    print (i)