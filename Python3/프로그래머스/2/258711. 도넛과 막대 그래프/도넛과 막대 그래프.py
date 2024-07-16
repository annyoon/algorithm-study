def solution(edges):
    result = [0, 0, 0, 0]
    dic = {}
    
    for edge in edges:
        for i in range(2):
            if edge[i] not in dic:
                dic[edge[i]] = [0, 0]
            dic[edge[i]][i] += 1
            
    for node in dic:
        if dic[node][0] >= 2 and dic[node][1] == 0:
            result[0] = node
        elif dic[node][0] == 2:
            result[3] += 1
        elif dic[node][0] == 0:
            result[2] += 1
            
    result[1] = dic[result[0]][0] - result[2] - result[3]
    
    return result
