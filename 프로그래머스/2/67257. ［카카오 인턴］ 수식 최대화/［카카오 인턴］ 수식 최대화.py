from itertools import permutations

def solution(expression):
    answer = 0
    arr, count = [], []
    tmp = ''
    for exp in expression:
        if exp.isdigit():
            tmp += exp
        else:
            if exp not in count:
                count.append(exp)
            arr.append(int(tmp))
            arr.append(exp)
            tmp = ''
    arr.append(int(tmp))
    
    for operator in list(permutations(count, len(count))):
        result = arr.copy()
        for op in operator:
            result = calculate(result, op)
        answer = max(answer, abs(result[0]))
    
    return answer
                    
def calculate(arr, op):
    result = []
    flag = False
    for i in range(len(arr)):
        if arr[i] == op:
            tmp = result.pop()
            flag = True
            if op == '+':
                result.append(tmp + arr[i + 1])
            elif op == '-':
                result.append(tmp - arr[i + 1])
            else:
                result.append(tmp * arr[i + 1])
        else:
            if flag:
                flag = False
            else:
                result.append(arr[i])
    return result
