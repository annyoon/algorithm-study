def solution(dartResult):
    bonus = {"S": 1, "D": 2, "T": 3}
    options = [""] * 3
    scores = []
    number = ""

    for d in dartResult:
        if not d.isalnum():
            options[len(scores) - 1] = d
        elif d.isalpha():
            scores.append(int(number) ** bonus[d])
            number = ""
        else:
            number += d

    for i in range(len(options)):
        if options[i] == "*":
            scores[i] *= 2
            if i > 0:
                scores[i - 1] *= 2
        elif options[i] == "#":
            scores[i] *= -1

    return sum(scores)
