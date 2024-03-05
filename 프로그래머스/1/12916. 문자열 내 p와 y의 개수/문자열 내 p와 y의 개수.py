def solution(s):
    answer = True
    pNum = s.count('p') + s.count('P')
    yNum = s.count('y') + s.count('Y')
    return pNum == yNum