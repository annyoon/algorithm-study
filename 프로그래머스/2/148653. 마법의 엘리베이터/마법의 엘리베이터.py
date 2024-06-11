def solution(storey):
    
    def solve(num):
        length = len(str(num)) - 1
        
        if length == 0:
            return min(num, 11 - num)
        
        sub = 10 ** (length + 1) - num
        
        result1 = num // (10 ** length) + solve(num % (10 ** length))
        result2 = 1 + sub // (10 ** length) + solve(sub % (10 ** length))
        
        return min(result1, result2)
    
    return solve(storey)
