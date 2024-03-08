from itertools import combinations

def solution(numbers):
    s = set()

    for c in combinations(numbers, 2):
        s.add(sum(c))

    return sorted(list(s))
