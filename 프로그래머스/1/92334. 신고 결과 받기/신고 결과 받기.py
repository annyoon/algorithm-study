def solution(id_list, report, k):
    dic, dic_report, result = {}, {}, {}
    for i in id_list:
        dic[i] = set()
        result[i] = 0
        
    for r in report:
        r = r.split(' ')
        dic[r[1]].add(r[0])
        
    for d in dic:
        dic_report[d] = len(dic[d])
        
    for d in dic_report:
        if dic_report[d] >= k:
            for user in dic[d]:
                result[user] += 1
                
    return [r for r in result.values()]
