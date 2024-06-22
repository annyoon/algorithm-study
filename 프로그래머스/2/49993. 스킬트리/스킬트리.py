def solution(skill, skill_trees):
    answer = 0
    
    for tree in skill_trees:
        string = ''
        for t in tree:
            if t in skill:
                string += t
        for i in range(len(skill) + 1):
            if string == skill[:i]:
                answer += 1
                break
    
    return answer
