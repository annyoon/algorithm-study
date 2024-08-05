minCount = 20

def solution(name):
    answer = 0
    for n in name:
        answer += min(ord(n) - ord('A'), ord('Z') - ord(n) + 1)
    
    if answer == 0:
        return answer
    
    solve(list(name), 0, '', 0)
    return answer + minCount
    
def solve(name, cur, pre, count):
    global minCount
    if name.count('A') == len(name):
        minCount = min(minCount, count - 1)
        return
    
    if name[cur] != 'A' or pre != 'right':
        newName = name[:]
        newName[cur] = 'A'
        right = cur + 1 if cur < len(name) - 1 else 0
        solve(newName, right, 'left', count + 1)
        
    if name[cur] != 'A' or pre != 'left':
        newName = name[:]
        newName[cur] = 'A'
        left = cur - 1 if cur > 0 else len(name) - 1
        solve(newName, left, 'right', count + 1)
