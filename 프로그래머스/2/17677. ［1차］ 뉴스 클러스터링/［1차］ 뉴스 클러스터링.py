import math

def solution(str1, str2):
    a, b = 0, 0
    dic1 = getDict(str1)
    dic2 = getDict(str2)
    
    for d in dic1:
        if d in dic2:
            a += min(dic1[d], dic2[d])
            b += max(dic1[d], dic2[d])
        else:
            b += dic1[d]
            
    for d in dic2:
        if d not in dic1:
            b += dic2[d]
            
    return 65536 if b == 0 else math.trunc(a / b * 65536)

def getDict(string):
    dic = {}
    string = string.upper()
    
    for i in range(len(string) - 1):
        if string[i].isalpha() and string[i + 1].isalpha():
            tmp = string[i] + string[i + 1]
            if tmp in dic:
                dic[tmp] += 1
            else:
                dic[tmp] = 1
                
    return dic
