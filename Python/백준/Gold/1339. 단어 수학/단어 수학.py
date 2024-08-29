import sys
N = int(sys.stdin.readline())
S = [sys.stdin.readline().strip() for _ in range(N)]
words = {} # 단어별 값을 지정
for s in S: 
    x = len(s)-1 # 10의 제곱을 해줄 값
    for i in s :
        if i in words:
            words[i] += 10**x # 있으면 x만큼 제곱한걸 더하고
        else :
            words[i] = 10**x # 없으면 x만큼 제곱해서 넣자
        x -= 1

words_sort = sorted(words.values(),reverse=True) # 딕셔너리의 value만 내림차순으로 가져오자
result = 0
num = 9
for k in words_sort:
    result += k * num # 내림차순 한거에 9부터 하나씩 곱해서 더해주자
    num -= 1
print(result)