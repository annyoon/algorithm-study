def solution(users, emoticons):
    answer = [0, 0]
    discount_list = []
    
    def get_discount(i, arr):
        if i == len(emoticons):
            discount_list.append(arr[:])
            return
        
        for p in [10, 20, 30, 40]:
            temp = [p, emoticons[i] * (100 - p) // 100] # 할인율, 할인된 가격
            arr.append(temp)
            get_discount(i + 1, arr)
            arr.pop()
            
    get_discount(0, [])
    
    for d in discount_list:
        plus, total = 0, 0
        
        for u in users:
            money = 0
            
            for i in range(len(d)):
                if d[i][0] >= u[0]:
                    money += d[i][1]
                    
            if money >= u[1]:
                plus += 1
            else:
                total += money
                
        if plus > answer[0]:
            answer = [plus, total]
        elif plus == answer[0]:
            answer = [plus, max(answer[1], total)]
            
    return answer
