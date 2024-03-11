def solution(N, stages):
    length = len(stages)
    arr = []

    for i in range(1, N + 1):
        cnt = stages.count(i)

        if length == 0:
            arr.append((i, 0))
        else:
            arr.append((i, cnt / length))

        length -= cnt

    arr.sort(key=lambda x: x[1], reverse=True)
    return [k for k, v in arr]
