def solution(cap, n, deliveries, pickups):
    answer = 0
    d, p = n - 1, n - 1
    
    while True:
        while d >= 0 and deliveries[d] == 0:
            d -= 1
        while p >= 0 and pickups[p] == 0:
            p -= 1
        if d < 0 and p < 0:
            break
            
        answer += (max(d, p) + 1) * 2
        
        for _ in range(cap):
            while d >= 0 and deliveries[d] == 0:
                d -= 1
            while p >= 0 and pickups[p] == 0:
                p -= 1
            if d >= 0:
                deliveries[d] -= 1
            if p >= 0:
                pickups[p] -= 1

    return answer
