# 답 참고

from collections import deque

n, k = map(int, input().split())
a = deque(map(int, input().split()))

robot = deque([0] * n)
answer = 0

while True:
    answer += 1

    a.rotate(1)
    robot[-1] = 0

    robot.rotate(1)
    robot[-1] = 0

    for i in range(n - 2, -1, -1):
        if a[i + 1] >= 1 and robot[i + 1] == 0 and robot[i] == 1:
            robot[i + 1] = 1
            robot[i] = 0
            a[i + 1] -= 1

    robot[-1] = 0

    if a[0] != 0 and robot[0] != 1:
        robot[0] = 1
        a[0] -= 1

    if a.count(0) >= k:
        break

print(answer)
