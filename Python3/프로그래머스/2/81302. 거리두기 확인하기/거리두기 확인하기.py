flag = False
visited = []
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

def solution(places):
    global flag, visited
    result = []
    
    for place in places:
        flag = False
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    visited = [[False] * 5 for _ in range(5)]
                    dfs([i, j], 0, place)
                if flag:
                    break
            if flag:
                break
        if flag:
            result.append(0)
        else:
            result.append(1)
        
    return result

def dfs(cur, depth, place):
    global flag
    
    if flag:
        return
    if 1 <= depth <= 2:
        if place[cur[0]][cur[1]] == 'P':
            flag = True
        if depth == 2:
            return
    
    visited[cur[0]][cur[1]] = True
    
    for i in range(4):
        nCur = [cur[0] + dx[i], cur[1] + dy[i]]
        if inRange(nCur) and not visited[nCur[0]][nCur[1]]:
            if place[nCur[0]][nCur[1]] != 'X':
                dfs(nCur, depth + 1, place)
        
def inRange(cur):
    return 0 <= cur[0] < 5 and 0 <= cur[1] < 5
