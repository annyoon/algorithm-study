answer = 0

def solution(number):
    combinations(number, 0, [])
    return answer

def combinations(number, start, picked):
    global answer
    
    if len(picked) == 3:
        if sum(picked) == 0:
            answer += 1
        return
    
    for i in range(start, len(number)):
        picked.append(number[i])
        combinations(number, i + 1, picked)
        picked.pop()