def solution(jobs):
    answer = 0
    n = len(jobs)
    jobs.sort(reverse = True)
    arr, cur = [], 0
    
    while len(jobs) > 0 or len(arr) > 0:
        flag = False
        while len(jobs) > 0:
            if jobs[len(jobs) - 1][0] > cur:
                break
            arr.append(jobs.pop())
            flag = True
        if len(arr) == 0:
            job = jobs.pop()
            answer += job[1]
            cur = job[0] + job[1]
        else:
            if flag:
                arr.sort(key = lambda x: -x[1])
            job = arr.pop()
            answer += cur - job[0] + job[1]
            cur += job[1]
    
    return answer // n
