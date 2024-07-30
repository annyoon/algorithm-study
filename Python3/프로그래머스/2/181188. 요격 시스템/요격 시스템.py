def solution(targets):
    cur, answer = 0, 0
    targets.sort(key = lambda x: x[1])
    
    for i in range(len(targets)):
        if cur <= targets[i][0]:
            cur = targets[i][1]
            answer += 1
            
    return answer
