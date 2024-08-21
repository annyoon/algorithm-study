# 답 참고

def solution(stones, k):
    left = 1
    right = max(stones) + 1
    while left < right - 1:
        mid = (left + right) // 2
        nowk = 0
        flag = True
        for stone in stones:
            if stone < mid:
                nowk+=1
            else:
                nowk = 0
            if nowk == k:
                flag = False
                break
        if flag:
            left = mid
        else:
            right = mid
    return left
