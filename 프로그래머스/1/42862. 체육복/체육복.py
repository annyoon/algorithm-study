def solution(n, lost, reserve):
    lost_set = set(lost)
    reserve_set = set(reserve)

    s = lost_set & reserve_set
    lost_set -= s
    reserve_set -= s

    for r in reserve_set:
        if r - 1 in lost_set:
            lost_set -= {r - 1}
        elif r + 1 in lost_set:
            lost_set -= {r + 1}

    return n - len(lost_set)
