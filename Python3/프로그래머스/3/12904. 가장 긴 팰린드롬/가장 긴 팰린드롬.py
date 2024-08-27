def solution(s):
    answer = 1
    
    for mid in range(len(s) - 1):
        answer = max(answer, solve(s, mid))
        
    return answer
    
def solve(s, mid):
    count1, count2 = 1, 0
    
    for i in range(1, min(mid, len(s) - mid - 1) + 1):
        if s[mid - i] == s[mid + i]:
            count1 += 2
        else:
            break
            
    for i in range(min(mid, len(s) - mid - 2) + 1):
        if s[mid - i] == s[mid + i + 1]:
            count2 += 2
        else:
            break
            
    return max(count1, count2)
