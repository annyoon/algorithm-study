import sys
sys.setrecursionlimit(10 ** 5)

board, visited = [], []
count = 0

def solution(n, wires):
    global board, visited, count
    result = 100
    board = [[False] * (n + 1) for _ in range(n + 1)]
    
    for wire in wires:
        board[wire[0]][wire[1]] = True
        board[wire[1]][wire[0]] = True
        
    for wire in wires:
        board[wire[0]][wire[1]] = False
        board[wire[1]][wire[0]] = False
        visited, counts = [False] * (n + 1), []
        
        for cur in range(1, n + 1):
            if not visited[cur]:
                count = 0
                dfs(n, cur)
                counts.append(count)
        result = min(result, abs(counts[0] - counts[1]))
        
        board[wire[0]][wire[1]] = True
        board[wire[1]][wire[0]] = True
    
    return result

def dfs(n, cur):
    global board, visited, count
    visited[cur] = True
    count += 1
    
    for nCur in range(n + 1):
        if board[cur][nCur] and not visited[nCur]:
            dfs(n, nCur)
