def solution(s):
    cnt1, cnt2 = 0, 0
    for cur in s:
        if cur == '(':
            cnt1 += 1
        else:
            cnt2 += 1
        if cnt1 < cnt2:
            return False
    if cnt1 != cnt2:
        return False
    return True
