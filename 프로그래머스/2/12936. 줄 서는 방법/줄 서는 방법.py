# 답 참고

import math

def solution(n, k):
    answer = []
    l = []
    k = k - 1
    for n in range(1, n + 1):
        l.append(n)
    
    while l:
        a = k // math.factorial(n - 1)
        answer.append(l[a])
        del l[a]
        
        k = k % math.factorial(n - 1)
        n -= 1
        
    return answer
