def solution(s):
    answer = ''
    arr = s.split(' ')
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if j % 2 == 0:
                answer += arr[i][j].upper()
            else:
                answer += arr[i][j].lower()
        answer += ' '
    return answer[:len(answer) - 1]