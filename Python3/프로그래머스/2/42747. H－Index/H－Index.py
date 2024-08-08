def solution(citations):
    citations.sort(reverse = True)
    
    if citations[0] == 0:
        return 0
    
    for i in range(len(citations)):
        if i + 1 >= citations[i] and len(citations) - i - 1 <= citations[i]:
            if i + 1 == citations[i] or citations[i - 1] == citations[i]:
                return citations[i]
            else:
                return i
    return len(citations)
