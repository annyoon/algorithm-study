def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            land[i][j] += max([land[i - 1][n] for n in range(4) if n != j])
            
    return max(land[len(land) - 1])
