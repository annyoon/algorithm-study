from collections import deque

def solution(priorities, location):
    q = deque([p for p in list(enumerate(priorities))])
    count = 0
    
    while len(q) > 1:
        elem = q.popleft()
        if elem[1] < max([e[1] for e in q]):
            q.append(elem)
        else:
            count += 1
            if elem[0] == location:
                return count
            
    return count + 1
            