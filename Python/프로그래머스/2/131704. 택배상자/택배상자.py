def solution(order):
    answer, cur = 0, 1
    save = []
    flag = False
    
    for o in order:
        if flag:
            return answer
        if len(save) > 0 and o == save[len(save) - 1]:
            save.pop()
            answer += 1
        else:
            while True:
                if o == cur:
                    cur += 1
                    answer += 1
                    break
                if cur > len(order):
                    flag = True
                    break
                save.append(cur)
                cur += 1
        
    return answer
