from itertools import combinations_with_replacement

def solution(n, info):
    score, result = 0, []
    for arr in list(combinations_with_replacement([i for i in range(11)], n)):
        a, b = 0, 0
        arr = convert(arr)
        for i in range(11):
            if info[i] == 0 and arr[i] == 0:
                continue
            elif info[i] >= arr[i]:
                a += 10 - i
            else:
                b += 10 - i
        if b - a > score:
            result = arr
            score = b - a
    return [-1] if len(result) == 0 else result

def convert(arr):
    result = [0] * 11
    for a in arr:
        result[10 - a] += 1
    return result
