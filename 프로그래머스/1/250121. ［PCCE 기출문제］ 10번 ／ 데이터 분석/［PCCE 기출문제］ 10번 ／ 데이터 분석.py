def solution(data, ext, val_ext, sort_by):
    dic = {'code':0, 'date':1, 'maximum':2, 'remain':3}
    idx = dic[ext]
    sort_idx = dic[sort_by]
    result = []
    
    for d in data:
        if d[idx] < val_ext:
            result.append(d)
            
    return sorted(result, key = lambda x: x[sort_idx])
