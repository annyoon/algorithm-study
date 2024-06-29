import heapq

def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)
    
    while len(scoville) > 1:
        score1 = heapq.heappop(scoville)
        if score1 >= K:
            return count
        score2 = heapq.heappop(scoville)

        new_score = score1 + score2 * 2
        heapq.heappush(scoville, new_score)
        count += 1
    
    if scoville[0] >= K:
        return count
    return -1
