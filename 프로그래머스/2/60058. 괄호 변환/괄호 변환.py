def solution(p):
    return solve(p)
    
def solve(v):
    if v == '':
        return v
    
    check = 0
    isRight = True
    
    for i in range(len(v)):
        if v[i] == '(':
            check += 1
        else:
            check -= 1
        if check < 0:
            isRight = False
        if check == 0:
            if isRight:
                return v[:i + 1] + solve(v[i + 1:])
            else:
                return '(' + solve(v[i + 1:]) + ')' + reverse(v[1:i])
            break
            
def reverse(u):
    result = ''
    for j in u:
        if j == '(':
            result += ')'
        else:
            result += '('
    return result
