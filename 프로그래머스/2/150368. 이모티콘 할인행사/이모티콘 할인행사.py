from itertools import product

def solution(users, emoticons):
    result = [0, 0]
    for discount in list(product([10, 20, 30, 40], repeat = len(emoticons))):
        tmp = [0, 0]
        dic = {10: 0, 20: 0, 30: 0, 40: 0}
        for i in range(len(emoticons)):
            dic[discount[i]] += emoticons[i] * (1 - discount[i] / 100)
        for user in users:
            money = 0
            for d in dic:
                if d >= user[0]:
                    money += dic[d]
            if money >= user[1]:
                tmp[0] += 1
            else:
                tmp[1] += money
        if tmp[0] > result[0]:
            result = tmp[:]
        if tmp[0] == result[0] and tmp[1] > result[1]:
            result = tmp[:]
    return result
