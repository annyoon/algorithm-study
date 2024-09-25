s = input()

def solve():
    if s[0] == '0':
        return 0
    if len(s) == 1:
        return 1
    if s[1] == '0' and int(s[0] + s[1]) > 26:
        return 0
    
    dp = [0] * len(s)
    dp[0] = 1
    dp[1] = 2 if s[1] != '0' and int(s[0] + s[1]) <= 26 else 1

    for i in range(2, len(s)):
        if s[i] == '0':
            if 0 < int(s[i - 1] + s[i]) <= 26:
                dp[i] = dp[i - 2]
            else:
                return 0
        elif s[i - 1] != '0' and int(s[i - 1] + s[i]) <= 26:
            dp[i] = dp[i - 1] + dp[i - 2]
        else:
            dp[i] = dp[i - 1]

    return dp[-1] % 10 ** 6

print(solve())
