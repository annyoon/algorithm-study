def solution(survey, choices):
    answer = ''
    type_dic = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    score = {1: [0, 3], 2: [0, 2], 3: [0, 1], 4: [0, 0], 5: [1, 1], 6: [1, 2], 7: [1, 3]}
    
    for i in range(len(survey)):
        s = score[choices[i]]
        type_dic[survey[i][s[0]]] += s[1]
    
    for type_c in ['TR', 'FC', 'MJ', 'NA']:
        max_num = max(type_dic[type_c[0]], type_dic[type_c[1]])
        for c in type_c:
            if type_dic[c] == max_num:
                tmp = c
        answer += tmp
    
    return answer
