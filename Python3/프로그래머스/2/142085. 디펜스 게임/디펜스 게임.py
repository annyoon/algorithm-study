import heapq

def solution(n, k, enemy):
    heap = []
    for i in range(len(enemy)):
        if enemy[i] <= n:
            n -= enemy[i]
            heapq.heappush(heap, -enemy[i])
        else:
            if k > 0:
                if len(heap) > 0:
                    tmp = -heapq.heappop(heap)
                    if enemy[i] < tmp:
                        n += tmp - enemy[i]
                        heapq.heappush(heap, -enemy[i])
                    else:
                        heapq.heappush(heap, -tmp)
                k -= 1
            else:
                return i
    return len(enemy)
