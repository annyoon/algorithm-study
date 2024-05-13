from collections import deque

def solution(queue1, queue2):
    answer = -1
    
    if (sum(queue1) + sum(queue2)) % 2 != 0:
        return answer
    
    d1, d2 = deque(queue1), deque(queue2)
    goal = (sum(queue1) + sum(queue2)) // 2
    
    sum_d = sum(d1)
    count = 0
        
    while(d2):
        if sum_d == goal:
            return count
        elif sum_d > goal:
            sum_d -= d1.popleft()
            count += 1
        else:
            tmp = d2.popleft()
            d1.append(tmp)
            sum_d += tmp
            count += 1
                
    if not d2:
        answer = -1
    else:
        answer = count
    
    return answer
