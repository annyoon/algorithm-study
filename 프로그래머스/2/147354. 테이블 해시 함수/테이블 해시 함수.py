def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key = lambda x: (x[col - 1], -x[0]))
    
    for i in range(row_begin, row_end + 1):
        s = 0
        for n in data[i - 1]:
            s += n % i
        answer = s if answer == 0 else answer ^ s
        
    return answer
