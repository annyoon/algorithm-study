# 답 참고

def solution(n):
    def check(ls, new):
        for i in range(len(ls)):
            if new == ls[i] or (len(ls) - i) == abs(ls[i] - new):
                return False
        return True
    
    def dfs(n, ls):
        if len(ls) == n:
            return 1
        cnt = 0
        for i in range(n):
            if check(ls, i):
                cnt += dfs(n, ls + [i])
        return cnt
        
    return dfs(n, [])
