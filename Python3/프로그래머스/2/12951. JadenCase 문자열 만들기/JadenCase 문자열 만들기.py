def solution(s):
    arr = s.split(' ')
    result = ''
    
    for i, a in enumerate(arr):
        if len(a) > 0:
            if not a[0].isdigit():
                result += a[0].upper()
            else:
                result += a[0]
            if len(a) > 1:
                result += a[1:].lower()
        if i != len(arr) - 1:
            result += ' '
        
    return result