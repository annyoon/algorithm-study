def solution(str1, str2):
    dic1 = makeDic(str1)
    dic2 = makeDic(str2)
    i, u = 0, 0
    
    for d in dic1:
        if d in dic2:
            i += min(dic1[d], dic2[d])
            u += max(dic1[d], dic2[d])
        else:
            u += dic1[d]
            
    for d in dic2:
        if d not in dic1:
            u += dic2[d]
    
    if u == 0:
        return 65536
            
    return int(float(i) / float(u) * 65536)
                
    
def makeDic(str):
    dic = {}
    for i in range(1, len(str)):
        s = str[i - 1] + str[i]
        if s.isalpha():
            if s.upper() in dic:
                dic[s.upper()] += 1
            else:
                dic[s.upper()] = 1  
    return dic
    