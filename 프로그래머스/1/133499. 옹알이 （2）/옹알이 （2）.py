combi = []

def solution(babbling):
    arr = ["aya", "ye", "woo", "ma"]
    fail = ["ayaaya", "yeye", "woowoo", "mama"]
    result = 0

    combinations(arr, fail, "")

    for b in babbling:
        if b in combi:
            result += 1

    return result

def combinations(arr, fail, picked):
    global combi

    for f in fail:
        if f in picked:
            return

    if len(picked) <= 30:
        combi.append(picked)
    else:
        return

    for i in range(0, len(arr)):
        combinations(arr, fail, picked + arr[i])
