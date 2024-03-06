def solution(x):
    num = 0
    for s in str(x):
        num += int(s)
    return x % num == 0