def solution(n, costs):
    result, parent = 0, []
    costs.sort(key = lambda x: x[2])
    
    for i in range(n + 1):
        parent.append(i)
    
    for cost in costs:
        a, b, c = cost
        if findParent(parent, a) != findParent(parent, b):
            unionParent(parent, a, b)
            result += c
            
    return result
        
def findParent(parent, x):
    if parent[x] != x:
        parent[x] = findParent(parent, parent[x])
    return parent[x]

def unionParent(parent, a, b):
    a = findParent(parent, a)
    b = findParent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
