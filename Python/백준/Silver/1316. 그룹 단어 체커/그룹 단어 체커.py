n = int(input())
words = [ input() for _ in range(n) ]

cnt = 0

for word in words:
    tmp = word[0]
    end_list = []

    for w in word:
        if w in end_list:
            cnt += 1
            break

        if w != tmp:
            end_list.append(tmp)
            tmp = w

answer = n - cnt
print(answer)
