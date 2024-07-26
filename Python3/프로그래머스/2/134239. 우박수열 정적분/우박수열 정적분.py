def solution(k, ranges):
    area, result = [], []
    n = 0
    
    while k > 1:
        if k % 2 == 0:
            nxt = k // 2
        else:
            nxt = k * 3 + 1
        area.append((k + nxt) / 2)
        k = nxt
        n += 1
        
    for r in ranges:
        if r[0] > r[1] + n:
            result.append(-1.0)
        else:
            result.append(sum(area[r[0]:r[1] + n]))
            
    return result
