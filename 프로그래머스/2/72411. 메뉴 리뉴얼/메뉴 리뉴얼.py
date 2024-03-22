from itertools import combinations

def solution(orders, course):
    result = []
    
    for c in course:
        dic = {}
        
        for order in orders:
            order = sorted(list(order))
            for combi in list(combinations(order, c)):
                combi = ''.join(list(combi))
                if combi in dic:
                    dic[combi] += 1
                else:
                    dic[combi] = 1
                    
        dic = dict(sorted(dic.items()))
        if len(dic) > 0:
            max_num = max(dic.values())
            
            if max_num >= 2:
                for d in dic:
                    if dic[d] == max_num:
                        result.append(d)
                    
    return sorted(result)