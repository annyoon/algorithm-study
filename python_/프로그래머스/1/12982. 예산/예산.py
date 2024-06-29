def solution(d, budget):
    answer = 0
    s = 0
    
    for i in sorted(d):
        s += i
        
        if budget - s < 0:
            break
        answer += 1
        
    return answer