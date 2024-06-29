def solution(orders, course):
    answer = []
    dic = {}
    
    def combination(i, menu, menu_num, combo):
        if len(combo) == menu_num:
            combo_str = ""
            
            for c in combo:
                combo_str += c
                
            menu_combo.append(combo_str)
            return
        
        for num in range(i, len(menu)):
            combo.append(menu[num])
            combination(num + 1, menu, menu_num, combo)
            combo.pop()
    
    for course_num in course:
        for order in orders:
            order_list = list(order)
            order_list.sort()
            
            menu_combo = []
            combination(0, order_list, course_num, [])
            
            for mc in menu_combo:
                if mc in dic:
                    dic[mc] += 1
                else:
                    dic[mc] = 1
    
    for course_num in course:
        dic_num = {}
        for d in dic:
            if len(d) == course_num:
                if dic[d] >= 2:
                    dic_num[d] = dic[d]
            
        tmp = [k for k,v in dic_num.items() if max(dic_num.values()) == v]
        
        for t in tmp:
            answer.append(t)
    
    return sorted(answer)
