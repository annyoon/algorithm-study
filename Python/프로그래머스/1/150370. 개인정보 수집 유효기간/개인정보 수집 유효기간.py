def solution(today, terms, privacies):
    dic = {}
    for term in terms:
        dic[term[0]] = int(term[2:]) * 28
        
    answer = []
    today = getDay(today)
    
    for i, p in list(enumerate(privacies, 1)):
        if today - getDay(p[:10]) >= dic[p[11]]:
            answer.append(i)
            
    return answer

def getDay(date):
    year = int(date[:4]) - 2000
    month = int(date[5:7]) - 1
    day = int(date[8:]) - 1
    
    return year * 28 * 12 + month * 28 + day
    