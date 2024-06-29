def solution(k, m, score):
    score.sort(reverse=True)
    box = []
    result = 0

    for s in score:
        if len(box) == m:
            result += min(box) * m
            box = [s]
        else:
            box.append(s)

    if len(box) == m:
        result += min(box) * m

    return result
