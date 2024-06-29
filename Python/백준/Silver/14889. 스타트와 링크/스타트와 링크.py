from itertools import combinations

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
answer = []

def calculate(arr):
    result = 0
    for cbn in list(combinations(arr, 2)):
        result += s[cbn[0]][cbn[1]] + s[cbn[1]][cbn[0]]

    return result

for arr in list(combinations([i for i in range(n)], n // 2)):
    dic = {}
    for a in arr:
        dic[a] = True

    opponent = []
    for i in range(n):
        if i not in dic:
            opponent.append(i)

    answer.append(abs(calculate(arr) - calculate(opponent)))

print(min(answer))
