import math

def solution(r1, r2):
    count = 0
    
    for x in range(r2):
        y2 = math.sqrt(r2 ** 2 - x ** 2)
        y1 = math.sqrt(r1 ** 2 - x ** 2) if r1 > x else 0
        
        count += math.floor(y2) - math.ceil(y1)
        count = count + 1 if y1 != 0 else count
        
    return count * 4
