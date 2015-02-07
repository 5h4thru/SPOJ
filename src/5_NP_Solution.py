n = int(input())
for i in range(n):
    string = input()
    length = len(string)
    ans = ""
    if length %2 == 0 :
        half = length // 2
        str_half = string[0:half]
        ans =  str_half + str_half[::-1]       
        #print (ans)  
        if(ans <= string):
            str_half = str(int(str_half) + 1)
            ans = str_half + (str_half[0:half])[::-1]
            #print(str_half, ans)
        print(ans)
    else:
        half = length // 2
        str_half = string[0:half]
        ans = str_half + string[half] + str_half[::-1]
        #print(ans)
        if(ans<= string):            
            str_half = str(int(str_half+string[half]) + 1)
            ans = str_half + (str_half[0:half])[::-1]
            #print(str_half, ans)
        print(ans)