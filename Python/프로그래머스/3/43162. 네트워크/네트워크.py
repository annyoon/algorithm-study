import sys
sys.setrecursionlimit(10 ** 5)

visited = []

def solution(n, computers):
    global visited
    visited = [False] * n
    answer = 0
    
    for cur in range(n):
        if not visited[cur]:
            answer += 1
            dfs(n, computers, cur)
            
    return answer
        
def dfs(n, computers, cur):
    global visited
    
    for num in range(n):
        if not visited[num] and computers[cur][num]:
            visited[num] = True
            dfs(n, computers, num)
            