def solution(lottos, win_nums):
    count = 0
    
    for num in lottos:
        if num in win_nums:
            count += 1
            
    return [getRank(count + lottos.count(0)), getRank(count)]
    
def getRank(count):
    if count < 2:
        return 6
    else:
        return 7 - count