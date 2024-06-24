def solution(phone_book):
    dic = {}
    for phone in phone_book:
        dic[phone] = True
    
    for phone in phone_book:
        for i in range(1, len(phone)):
            if phone[:i] in dic:
                return False
    return True
