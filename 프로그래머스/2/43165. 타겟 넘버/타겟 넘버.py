answer = 0
sum_numbers = 0

def solution(numbers, target):
    global answer, sum_numbers
    
    sum_numbers = sum(numbers)
    
    for d in range(len(numbers) + 1):
        dfs(numbers, target, 0, d, [])
    
    return answer

def dfs(numbers, target, start, depth, arr):
    global answer, sum_numbers
    
    if len(arr) == depth:
        num = sum([numbers[i] for i in arr])
        tmp = sum_numbers - 2 * (num)
        
        if tmp == target:
            answer += 1
        
        return
    
    for i in range(start, len(numbers)):
        arr.append(i)
        dfs(numbers, target, i + 1, depth, arr)
        arr.pop()