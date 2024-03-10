def solution(k, score):
    answer = []
    arr = []
    
    for s in score:
        if len(arr) < k:
            arr.append(s)
        else:
            if s > min(arr):
                arr.remove(min(arr))
                arr.append(s)
        answer.append(min(arr))
    return answer