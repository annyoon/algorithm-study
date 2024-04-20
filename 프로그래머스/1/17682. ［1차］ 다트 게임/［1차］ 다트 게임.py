def solution(dartResult):
    arr = []
    number = ''
    alpha = {'S': 1, 'D': 2, 'T': 3}
    
    for d in dartResult:
        if d.isdigit():
            number += d
        elif d.isalpha():
            arr.append(int(number) ** alpha[d])
            number = ''
        elif d == '*':
            arr[len(arr) - 1] *= 2
            if len(arr) > 1:
                arr[len(arr) -2] *= 2
        elif d == '#':
            arr[len(arr) - 1] *= (-1)
                
    return sum(arr)
