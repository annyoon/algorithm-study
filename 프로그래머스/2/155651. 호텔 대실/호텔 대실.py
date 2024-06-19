def solution(book_time):
    def convert(time):
        return int(time[:2]) * 60 + int(time[3:])
        
    dic = {}
    answer = 0
    
    for i in range(len(book_time)):
        book_time[i][0] = convert(book_time[i][0])
        book_time[i][1] = convert(book_time[i][1])
        t = book_time[i]
        
        if tuple(t) in dic:
            dic[tuple(t)] += 1
        else:
            dic[tuple(t)] = 1
            
    book_time.sort(key = lambda x: (x[0], x[1] - x[0]))
    
    def solve(idx):
        end_time = book_time[idx][1] + 10
        for i in range(idx + 1, len(book_time)):
            if book_time[i][0] >= end_time and dic[tuple(book_time[i])] > 0:
                dic[tuple(book_time[i])] -= 1
                solve(i)
                break
                
    for i in range(len(book_time)):
        if dic[tuple(book_time[i])] > 0:
            dic[tuple(book_time[i])] -= 1
            solve(i)
            answer += 1
            
    return answer
