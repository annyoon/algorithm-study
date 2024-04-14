def solution(s):
    arr, answer = [], []
    
    for elem in s.split('}'):
        a = []
        for e in elem.split(','):
            if len(e) != 0:
                a.append(int(e.strip('{')))
        arr.append(a)
            
    idx_arr = list(enumerate(map(len, arr)))
    idx_arr.sort(key = lambda x : (x[1]))
    
    dic = {}
    
    for n in arr[idx_arr[len(idx_arr) - 1][0]]:
        dic[n] = True
        
    for n in idx_arr:
        for a in arr[n[0]]:
            if dic[a]:
                answer.append(a)
                dic[a] = False
                break
                
    return answer