indexArr = []

def solution(k, dungeons):
    global indexArr
    n = len(dungeons)
    result = 0
    
    for depth in range(1, n + 1):
        indexArr = []
        solve(n, depth, [], [False] * n)
        
        if check(k, dungeons):
            result = depth
            
    return result

def solve(n, depth, arr, visited):
    if len(arr) == depth:
        indexArr.append(arr[:])
        return
    
    for i in range(n):
        if not visited[i]:
            arr.append(i)
            visited[i] = True
            solve(n, depth, arr, visited)
            arr.pop()
            visited[i] = False
            
def check(k, dungeons):
    for arr in indexArr:
        count, score = 0, k
        for i in arr:
            if score >= dungeons[i][0]:
                count += 1
                score -= dungeons[i][1]
        if count == len(arr):
            return True
    return False
