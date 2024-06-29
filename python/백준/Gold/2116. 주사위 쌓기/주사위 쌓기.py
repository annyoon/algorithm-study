import sys
sys.setrecursionlimit(6 * 10000)

n = int(input())
dices = [list(map(int, input().split())) for _ in range(n)]
otherside = {0: 5, 5: 0, 1: 3, 3: 1, 2: 4, 4: 2}
result = 0

def solve(idx, bottomIdx):
    sideMax = max([dices[idx][j] for j in range(6) if j != bottomIdx and j != otherside[bottomIdx]])
    if idx != n - 1:
        nextBottomIdx = -1
        for i in range(6):
            if dices[idx + 1][i] == dices[idx][bottomIdx]:
                nextBottomIdx = otherside[i]
                break
        return sideMax + solve(idx + 1, nextBottomIdx)
    else:
        return sideMax

for i in range(6):
    result = max(result, solve(0, i))
print(result)
