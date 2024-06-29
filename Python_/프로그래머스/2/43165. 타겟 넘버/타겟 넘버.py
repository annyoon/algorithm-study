result = 0

def solution(numbers, target):
    solve(numbers, target, 0, 0)
    
    return result
    
def solve(numbers, target, i, num):
    global result
    
    if i == len(numbers):
        if num == target:
            result += 1
        return
    
    solve(numbers, target, i + 1, num + numbers[i])
    solve(numbers, target, i + 1, num - numbers[i])