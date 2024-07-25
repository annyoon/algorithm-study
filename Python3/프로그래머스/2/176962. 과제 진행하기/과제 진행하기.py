from collections import deque

def solution(plans):
    result = []
    plans = [[p[0], convert(p[1]), int(p[2])] for p in plans]
    plans.sort(key = lambda x: x[1])
    q = deque()
    
    for i in range(len(plans) - 1):
        if plans[i][1] + plans[i][2] > plans[i + 1][1]:
            q.append([plans[i][0], plans[i][1] + plans[i][2] - plans[i + 1][1]])
        elif plans[i][1] + plans[i][2] < plans[i + 1][1]:
            result.append(plans[i][0])
            rest = plans[i + 1][1] - (plans[i][1] + plans[i][2])
            while q and rest > 0:
                tmp = q.pop()
                if tmp[1] > rest:
                    q.append([tmp[0], tmp[1] - rest])
                else:
                    result.append(tmp[0])
                rest -= tmp[1]
        else:
            result.append(plans[i][0])
        
    result.append(plans[len(plans) - 1][0])
    while q:
        result.append(q.pop()[0])
        
    return result

def convert(time):
    return int(time[:2]) * 60 + int(time[3:])
