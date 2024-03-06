def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        sign = 1 if signs[i] else -1
        answer += absolutes[i] * sign
    return answer