def solution(keymap, targets):
    dic = {}
    for i in range(26):
        dic[chr(ord('A') + i)] = 101
        
    for letter in dic:
        for key in keymap:
            for i in range(len(key)):
                if key[i] == letter:
                    dic[letter] = min(i + 1, dic[letter])
                    break
                    
    result = []
    for target in targets:
        result.append(getResult(dic, target))
            
    return result

def getResult(dic, string):
    num = 0
    for s in string:
        if dic[s] == 101:
            return -1
        num += dic[s]
    return num