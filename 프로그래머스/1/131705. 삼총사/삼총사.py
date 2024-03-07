from itertools import combinations

def solution(number):
    answer = 0
    for d in combinations(number, 3):
        if sum(d) == 0:
            answer += 1
            
    return answer