def solution(friends, gifts):
    dic = {}
    
    n = 0
    for f in friends:
        dic[f] = n
        n += 1
        
    length = len(friends)
    arr = [[0] * length for _ in range(length)]
        
    for gift in gifts:
        g = gift.split(' ')
        arr[dic[g[0]]][dic[g[1]]] += 1
        
    gift_num = [0] * length
    
    for d in dic:
        i = dic[d]
        a = sum([arr[i][idx] for idx in range(length)])
        b = sum([arr[idx][i] for idx in range(length)])
        gift_num[i] = a - b
        
    result = [0] * length
        
    for i in range(length):
        for j in range(i + 1, length):
            if arr[i][j] > arr[j][i]:
                result[i] += 1
            elif arr[i][j] < arr[j][i]:
                result[j] += 1
            else:
                if gift_num[i] > gift_num[j]:
                    result[i] += 1
                if gift_num[i] < gift_num[j]:
                    result[j] += 1
                    
    return max(result)
            