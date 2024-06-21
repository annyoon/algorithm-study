def solution(sequence, k):
    left, right = 0, 0
    num = sequence[0]
    result = [0, 2000000]
    
    while left <= right:
        if num < k:
            if right < len(sequence) - 1:
                right += 1
                num += sequence[right]
            else:
                break
        elif num > k:
            num -= sequence[left]
            left += 1
        elif num == k:
            if result[1] - result[0] > right - left:
                result = [left, right]
            if right < len(sequence) - 1:
                right += 1
                num += sequence[right]
            else:
                break
    return result
