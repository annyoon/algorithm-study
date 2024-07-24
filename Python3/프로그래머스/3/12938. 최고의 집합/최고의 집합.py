import math

def solution(n, s):
    div, mod = divmod(s, n)
    
    if div == 0:
        return [-1]
    
    answer = [div] * n
    
    for i in range(mod):
        answer[len(answer) - 1 - i] += 1
        
    return answer
