def solution(n):
    answer = []
    string = str(n)
    for i in range(len(string) - 1, -1, -1):
        answer.append(int(string[i]))
    return answer