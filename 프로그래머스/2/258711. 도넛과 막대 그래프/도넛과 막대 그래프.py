def solution(edges):
    answer = [0, 0, 0, 0]
    nodeCnt = dict({})
    
    for edge in edges:
        a, b = edge[0], edge[1]

        if not nodeCnt.get(a):
            nodeCnt[a] = [0, 0]
        if not nodeCnt.get(b):
            nodeCnt[b] = [0, 0]
        nodeCnt[a][0] += 1
        nodeCnt[b][1] += 1

    for key, cnts in nodeCnt.items():
        if cnts[0] >= 2 and cnts[1] == 0:
            answer[0] = key
        elif cnts[0] == 0 and cnts[1] > 0:
            answer[2] += 1
        elif cnts[0] >= 2 and cnts[1] >= 2:
            answer[3] += 1

    answer[1] = nodeCnt[answer[0]][0] - answer[2] - answer[3]
    
    return answer
