def solution(triangle):
    dp = [triangle[0]]
    
    for i in range(1, len(triangle)):
        arr = []
        for j in range(len(triangle[i])):
            if j - 1 < 0:
                arr.append(triangle[i][j] + dp[i - 1][j])
            elif j == i:
                arr.append(triangle[i][j] + dp[i - 1][j - 1])
            else:
                arr.append(triangle[i][j] + max(dp[i - 1][j - 1], dp[i - 1][j]))
        dp.append(arr)
        
    return max(dp[len(dp) - 1])
