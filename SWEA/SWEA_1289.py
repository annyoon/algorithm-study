T = int(input())

for test_case in range(1, T + 1):
    memory = input()

    cnt = 0
    state = '0'

    for m in memory:
        if state == '0':
            if m == '1':
                cnt += 1
                state = '1'
        else:
            if m == '0':
                cnt += 1
                state = '0'

    print(f'#{test_case} {cnt}')
    