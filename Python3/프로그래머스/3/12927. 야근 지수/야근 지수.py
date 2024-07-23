import heapq

def solution(n, works):
    heap, answer = [], 0
    
    for work in works:
        heapq.heappush(heap, -work)
    
    for _ in range(n):
        num = -heapq.heappop(heap)
        num = 0 if num == 0 else 1 - num
        heapq.heappush(heap, num)
        
    for h in heap:
        answer += h ** 2
        
    return answer
