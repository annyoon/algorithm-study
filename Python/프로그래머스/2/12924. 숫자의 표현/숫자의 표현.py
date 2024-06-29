def solution(n):
    result = 1
    
    for i in range(1, n + 1):
        num = 0
        for j in range(i, n + 1):
            if num > n:
                break
            elif num == n:
                result += 1
                break
            num += j
            
    return result