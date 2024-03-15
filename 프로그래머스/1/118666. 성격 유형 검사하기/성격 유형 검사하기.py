def solution(survey, choices):
    person = {'R':0, 'T':0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    score = {1:[0, 3], 2:[0, 2], 3:[0, 1], 4:[0, 0], 5:[1, 1], 6:[1, 2], 7:[1, 3]}
    
    for i in range(len(survey)):
        s = score[choices[i]]
        person[survey[i][s[0]]] += s[1]
        
    result = ''
    
    for p in ['RT', 'CF', 'JM', 'AN']:
        num = max(person[p[0]], person[p[1]])
        for alp in p:
            if person[alp] == num:
                result += alp
                break
    
    return result