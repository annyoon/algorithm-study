S = input()
T = input()
answer = 0

def solve(cur):
    global answer
    
    if len(cur) == len(S):
        if ''.join(cur) == S:
            answer = 1
        return
    
    alp = cur.pop()
    if alp == 'A':
        solve(cur)
    cur.append(alp)
    if cur[0] == 'B':
        solve(cur[:0:-1])

solve(list(T))
print(answer)
