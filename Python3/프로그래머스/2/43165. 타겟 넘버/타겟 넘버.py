count = 0

def solution(numbers, target):
    solve(0, 0, numbers, target)
    return count
    
def solve(cur, idx, numbers, target):
    global count
    
    if idx >= len(numbers):
        if cur == target:
            count += 1
        return
    solve(cur + numbers[idx], idx + 1, numbers, target)
    solve(cur - numbers[idx], idx + 1, numbers, target)
