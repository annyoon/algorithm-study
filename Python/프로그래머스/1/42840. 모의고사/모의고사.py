def solution(answers):
    n1 = [1, 2, 3, 4, 5]
    n2 = [2, 1, 2, 3, 2, 4, 2, 5]
    n3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    dic = {1: 0, 2: 0, 3: 0}

    for i in range(len(answers)):
        if answers[i] == n1[i % len(n1)]:
            dic[1] += 1
        if answers[i] == n2[i % len(n2)]:
            dic[2] += 1
        if answers[i] == n3[i % len(n3)]:
            dic[3] += 1

    max_score = max(dic.values())

    answer = []
    for d in dic:
        if dic[d] == max_score:
            answer.append(d)

    return answer
