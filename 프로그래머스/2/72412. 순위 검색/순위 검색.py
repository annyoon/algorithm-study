# 답 참고

def solution(info, query):
    dic = dict()
    for a in ['cpp', 'java', 'python', '-']:
        for b in ['backend', 'frontend', '-']:
            for c in ['junior', 'senior', '-']:
                for d in ['chicken', 'pizza', '-']:
                    dic.setdefault((a, b, c, d), list())

    for i in info:
        i = i.split()
        for a in [i[0], '-']:
            for b in [i[1], '-']:
                for c in [i[2], '-']:
                    for d in [i[3], '-']:
                        dic[(a, b, c, d)].append(int(i[4]))

    for k in dic:
        dic[k].sort()

    answer = list()

    for q in query:
        q = q.split()
        scores = dic[(q[0], q[2], q[4], q[6])]
        std = int(q[7])
        l, r = 0, len(scores)
        
        while l < r:
            mid = (l + r) // 2
            if scores[mid] >= std:
                r = mid
            else:
                l = mid + 1
                
        answer.append(len(scores) - l)
        
    return answer
