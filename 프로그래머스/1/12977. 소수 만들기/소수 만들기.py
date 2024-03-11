answer = 0

def solution(nums):
    combinations(nums, 0, [])
    return answer

def combinations(nums, start, picked):
    global answer

    if len(picked) == 3:
        if isPirme(sum(picked)):
            answer += 1
        return

    for i in range(start, len(nums)):
        picked.append(nums[i])
        combinations(nums, i + 1, picked)
        picked.pop()

def isPirme(num):
    for i in range(2, int(num ** (1 / 2)) + 1):
        if num % i == 0:
            return False
    return True
