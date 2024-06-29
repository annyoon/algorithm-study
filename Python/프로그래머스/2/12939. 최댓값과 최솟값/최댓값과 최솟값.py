def solution(s):
    arr = list(map(int, s.split(' ')))
    result = str(min(arr)) + ' ' + str(max(arr))
    
    return result
