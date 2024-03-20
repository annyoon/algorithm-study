import math

def solution(fees, records):
    dic = {}
    dic_fee = {}
    
    for record in records:
        arr = record.split(' ')
        if arr[1] not in dic or dic[arr[1]] == -1:
            dic[arr[1]] = int(arr[0][:2]) * 60 + int(arr[0][3:])
        else:
            tmp = int(arr[0][:2]) * 60 + int(arr[0][3:]) - dic[arr[1]]
            if arr[1] not in dic_fee:
                dic_fee[arr[1]] = tmp
            else:
                dic_fee[arr[1]] += tmp
            dic[arr[1]] = -1
    print(dic)
            
    for d in dic:
        if dic[d] != -1:
            tmp = 23 * 60 + 59 - dic[d]
            if d not in dic_fee:
                dic_fee[d] = tmp
            else:
                dic_fee[d] += tmp
                
    dic_fee = dict(sorted(dic_fee.items()))
    print(dic_fee)
    
    result = []
    
    for d in dic_fee.values():
        if d <= fees[0]:
            result.append(fees[1])
        else:
            tmp = fees[1] + math.ceil(float(d - fees[0]) / float(fees[2])) * fees[3]
            result.append(tmp)
                         
    return result