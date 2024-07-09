def solution(picks, minerals):
    score = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]
    arr = []
    dia, iron, stone = 0, 0, 0
    result = 0
    
    for i in range(len(minerals)):
        if minerals[i] == 'diamond':
            dia += 1
        elif minerals[i] == 'iron':
            iron += 1
        else:
            stone += 1
        
        if i % 5 == 4:
            arr.append([dia, iron, stone])
            dia, iron, stone = 0, 0, 0
            
    if dia != 0 or iron != 0 or stone != 0:
        arr.append([dia, iron, stone])
        
    length = sum(picks)
    if len(arr) > length:
        arr = arr[:length]
    arr.sort(key = lambda x: (x[0], x[1], x[2]), reverse = True)
    
    idx = 0
    for i in range(3):
        for _ in range(picks[i]):
            for j in range(3):
                result += score[i][j] * arr[idx][j]
            idx += 1
            if idx == len(arr):
                return result
            
    return result
