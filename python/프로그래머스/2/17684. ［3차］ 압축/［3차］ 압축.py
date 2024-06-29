def solution(msg):
    dic = {}
    for i in range(26):
        dic[chr(ord('A') + i)] = i + 1
        
    arr, answer = [], []
    num = 27
    
    for i in range(len(msg)):
        arr.append(msg[i])
        w = ''.join(arr)
        
        if w not in dic:
            dic[w] = num
            num += 1
            
            c = arr.pop()
            answer.append(dic[''.join(arr)])
            arr = [c]
            
    answer.append(dic[''.join(arr)])
    return answer
