def solution(name, yearning, photo):
    answer = []
    dic = {}

    for i in range(len(name)):
        dic[name[i]] = yearning[i]

    for p in photo:
        score = 0
        for n in p:
            if n in dic:
                score += dic[n]
        answer.append(score)

    return answer
