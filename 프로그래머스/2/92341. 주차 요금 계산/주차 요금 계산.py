import math

def solution(fees, records):
    dic = {}
    check = {}
    
    for record in records:
        time = int(record[:2]) * 60 + int(record[3:5])
        car = record[6:10]
        if car in check and check[car] != -1:
            time -= check[car]
            check[car] = -1
            
            if car in dic:
                dic[car] += time
            else:
                dic[car] = time
        else:
            check[car] = time
            
    for car in check:
        if check[car] != -1:
            time = 23 * 60 + 59
            time -= check[car]
            if car in dic:
                dic[car] += time
            else:
                dic[car] = time
            
    for d in dic:
        if dic[d] <= fees[0]:
            dic[d] = fees[1]
        else:
            dic[d] = fees[1] + math.ceil((dic[d] - fees[0]) / fees[2]) * fees[3]

    return [v for v in dict(sorted(dic.items())).values()]
