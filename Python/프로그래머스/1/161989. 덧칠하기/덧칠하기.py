def solution(n, m, section):
    start = section[0]
    answer = 1
    
    for s in section:
        if s - start >= m:
            start = s
            answer += 1
            
    return answer
