def solution(s, n):
    answer = ''
    
    for a in s:
        if a == ' ':
            answer += a
            continue
            
        if ord('A') <= ord(a) <= ord('Z'):
            new_a = ord(a) + n if ord(a) + n <= ord('Z') else ord(a) + n - 26
        else:
            new_a = ord(a) + n if ord(a) + n <= ord('z') else ord(a) + n - 26
        answer += chr(new_a)
            
    return answer