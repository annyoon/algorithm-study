import math

def solution(fees, records):
    answer = []
    dic, dic_time = {}, {}
    
    def to_minute(s):
        return int(s[:2]) * 60 + int(s[3:5])
    
    def charge_fees(t):
        if t <= fees[0]:
            return fees[1]
        else:
            return fees[1] + math.ceil((t - fees[0]) / fees[2]) * fees[3]
        
    for r in records:
        time, car_num, stat = r.split(' ')
        
        if car_num not in dic:
            dic[car_num] = to_minute(time)
        else:
            if car_num not in dic_time:
                dic_time[car_num] = to_minute(time) - dic[car_num]
            else:
                dic_time[car_num] += to_minute(time) - dic[car_num]
            del dic[car_num]
            
    for d in dic:
        if d not in dic_time:
            dic_time[d] = 23 * 60 + 59 - dic[d]
        else:
            dic_time[d] += 23 * 60 + 59 - dic[d]
    
    dic_time_sorted = dict(sorted(dic_time.items()))
    
    for t in dic_time_sorted:
        answer.append(charge_fees(dic_time_sorted[t]))
    
    return answer