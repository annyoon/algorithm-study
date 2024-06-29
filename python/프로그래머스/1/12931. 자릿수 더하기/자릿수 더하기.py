def solution(n):
    answer = 0
    string = str(n)
    for i in string:
        answer += int(i)
    return answer