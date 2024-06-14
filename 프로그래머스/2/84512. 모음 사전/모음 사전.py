from itertools import product

def solution(word):
    dic = []
    answer = 1
    
    for i in range(1, 6):
        for p in list(product(['A', 'E', 'I', 'O', 'U'], repeat = i)):
            dic.append(''.join(p))
    
    for d in sorted(dic):
        if d == word:
            return answer
        answer += 1
