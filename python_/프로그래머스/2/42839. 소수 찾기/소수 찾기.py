import math
from itertools import permutations

def solution(numbers):
    def isPrimeNum(x):
        if x <= 1:
            return False
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True
    
    count = 0
    numbers = list(numbers)
    dic = {}
    
    for i in range(1, len(numbers) + 1):
        for num in list(permutations(numbers, i)):
            num = int(''.join(num))
            if isPrimeNum(num) and num not in dic:
                dic[num] = True
                count += 1
                
    return count
