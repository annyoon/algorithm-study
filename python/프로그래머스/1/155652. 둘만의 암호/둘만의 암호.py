def convert(alp, skip, index):
    while index:
        alp = chr(ord(alp) + 1)
        if ord(alp) == ord('z') + 1:
            alp = 'a'
        if alp not in skip:
            index -= 1
    return alp
        

def solution(s, skip, index):
    result = ''
    for alp in s:
        result += convert(alp, skip, index)
        
    return result
