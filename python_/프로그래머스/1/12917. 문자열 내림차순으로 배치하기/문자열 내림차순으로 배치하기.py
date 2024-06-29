def solution(s):
    arr = sorted(list(map(ord, s)), reverse = True)
    return ''.join(list(map(chr, arr)))