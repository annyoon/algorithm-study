from collections import deque

def solution(ingredient):
    dq = deque()
    
    for i in ingredient:
        dq.append(i)
        if len(dq) >= 4:
            tmp = ''
            for _ in range(4):
                tmp += str(dq.pop())
            if tmp != '1321':
                dq.extend(tmp[::-1])
            
    return (len(ingredient) - len(dq)) // 4
