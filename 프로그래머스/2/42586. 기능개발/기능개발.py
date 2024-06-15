import math

def solution(progresses, speeds):
    arr, answer = [], []
    
    for i in range(len(progresses)):
        arr.append(math.ceil((100 - progresses[i]) / speeds[i]))
        
    start = arr[0]
    count = 0
    
    for a in arr:
        if a <= start:
            count += 1
        else:
            answer.append(count)
            start = a
            count = 1
    answer.append(count)
    
    return answer
