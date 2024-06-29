from collections import deque

def solution(priorities, location):
    p = max(priorities)
    q = deque(list(enumerate(priorities)))
    count = 1
    
    while True:
        cur = q.popleft()
        if cur[1] == p:
            if cur[0] == location:
                return count
            p = max([n[1] for n in q])
            count += 1
        else:
            q.append(cur)
