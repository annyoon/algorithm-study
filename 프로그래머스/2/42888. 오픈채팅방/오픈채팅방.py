def solution(record):
    answer = []
    dic, arr = {}, []
    
    for r in record:
        if r[:5] == 'Leave':
            stat, uid = r.split()
        else:
            stat, uid, name = r.split()
        
        if stat == 'Enter':
            arr.append([stat, uid])
            dic[uid] = name
        elif stat == 'Leave':
            arr.append([stat, uid])
        else:
            dic[uid] = name
            
    for a in arr:
        if a[0] == 'Enter':
            answer.append('{}님이 들어왔습니다.'.format(dic[a[1]]))
        else:
            answer.append('{}님이 나갔습니다.'.format(dic[a[1]]))
    
    return answer
