def solution(s):
    result = [0, 0]
    while s != '1':
        tmp = s
        s = s.replace('0', '')
        result[1] += len(tmp) - len(s)
        s = str(bin(len(s)))[2:]
        result[0] += 1
    return result
