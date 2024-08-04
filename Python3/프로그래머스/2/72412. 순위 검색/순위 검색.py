# 답 참고

def solution(info, query):
    data = dict()
    for a in ['cpp', 'java', 'python', '-']:
        for b in ['backend', 'frontend', '-']:
            for c in ['junior', 'senior', '-']:
                for d in ['chicken', 'pizza', '-']:
                    data.setdefault((a, b, c, d), list())

    for i in info:
        i = i.split()
        for a in [i[0], '-']:
            for b in [i[1], '-']:
                for c in [i[2], '-']:
                    for d in [i[3], '-']:
                        data[(a, b, c, d)].append(int(i[4]))
                        
    for k in data:
        data[k].sort()

    answer = list()

    for q in query:
        q = q.split()
        scores = data[(q[0], q[2], q[4], q[6])]
        wanted = int(q[7])
        l,r = 0, len(scores)
        while l < r:
            middle = (l + r)//2
            if scores[middle] >= wanted:
                r = middle
            else:
                l = middle + 1
        answer.append(len(scores)-l)
        
    return answer
