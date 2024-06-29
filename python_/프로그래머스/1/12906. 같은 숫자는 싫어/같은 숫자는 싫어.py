def solution(arr):
    answer = []
    for a in arr:
        if len(answer) == 0 or a != answer[len(answer) - 1]:
            answer.append(a)
    return answer