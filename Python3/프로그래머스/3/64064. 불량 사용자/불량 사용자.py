result = []

def solution(user_id, banned_id):
    dic = {}
    candidates = []
    
    for banned in banned_id:
        id_list = []
        for user in user_id:
            if isSame(banned, user):
                id_list.append(user)
        candidates.append(id_list)
        
    pick(candidates, 0, [])
    
    return len(result)

def isSame(banned, user):
    if len(banned) != len(user):
        return False
    for i in range(len(banned)):
        if banned[i] != '*' and banned[i] != user[i]:
            return False
    return True

def pick(candidates, idx, picked):
    if idx == len(candidates):
        picked.sort()
        if picked not in result:
            result.append(picked)
        return
    for i in range(len(candidates[idx])):
        if candidates[idx][i] not in picked:
            picked.append(candidates[idx][i])
            pick(candidates, idx + 1, picked[:])
            picked.pop()
