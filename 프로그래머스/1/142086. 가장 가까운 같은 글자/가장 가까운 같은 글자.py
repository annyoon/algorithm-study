def solution(s):
    answer = []
    dic = {}
    
    for i in range(ord('a'), ord('z') + 1):
        dic[chr(i)] = -1
    
    for i in range(len(s)):
        if dic[s[i]] == -1:
            answer.append(-1)
        else:
            answer.append(i - dic[s[i]])
        dic[s[i]] = i
            
    return answer