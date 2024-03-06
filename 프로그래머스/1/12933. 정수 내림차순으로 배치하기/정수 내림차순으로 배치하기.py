def solution(n):
    answer = ''
    arr = [0] * 10
    for s in str(n):
        arr[int(s)] += 1
    for i in range(9, -1, -1):
        for j in range(arr[i]):
            answer += str(i)
    return int(answer)