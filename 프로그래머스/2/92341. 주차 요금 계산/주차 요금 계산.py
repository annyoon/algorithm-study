import math

def solution(fees, records):
    dic = {}
    dic_time = {}
    
    for record in records:
        r = record.split(' ')
        car = r[1]
        time = int(r[0][:2]) * 60 + int(r[0][3:])
        
        if car not in dic or dic[car] == -1:
            dic[car] = time
        else:
            cal = time - dic[car]
            if car in dic_time:
                dic_time[car] += cal
            else:
                dic_time[car] = cal
            dic[car] = -1
        
    for d in dic:
        if dic[d] != -1:
            cal = 23 * 60 + 59 - dic[d]
            if d in dic_time:
                dic_time[d] += cal
            else:
                dic_time[d] = cal
            
    for d in dic_time:
        if dic_time[d] <= fees[0]:
            dic_time[d] = fees[1]
        else:
            fee = fees[1] + math.ceil(float(dic_time[d] - fees[0]) / float(fees[2])) * fees[3]
            dic_time[d] = fee
            
    arr = sorted(dic_time.items())
    return [a[1] for a in arr]