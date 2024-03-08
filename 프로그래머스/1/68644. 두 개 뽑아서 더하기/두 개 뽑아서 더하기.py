s = set()

def solution(numbers):
    combinations(numbers, 0, [])
    return sorted(list(s))

def combinations(numbers, start, picked):
    global s

    if len(picked) == 2:
        s.add(sum(picked))
        return

    for i in range(start, len(numbers)):
        picked.append(numbers[i])
        combinations(numbers, i + 1, picked)
        picked.pop()
