def solution(players, callings):
    dic = {}
    for i in range(len(players)):
        dic[players[i]] = i
        
    for c in callings:
        idx = dic[c]
        looser = players[idx - 1]
        looser_idx = dic[looser]
        
        tmp = dic[c]
        dic[c] = dic[looser]
        dic[looser] = tmp
        
        tmp = players[idx]
        players[idx] = players[looser_idx]
        players[looser_idx] = tmp
        
    return players
