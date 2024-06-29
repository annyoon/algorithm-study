def solution(sizes):
    w = 0
    h = 0
    
    for size in sizes:
        w1, w2 = max(w, size[0]), max(w, size[1])
        h1, h2 = max(h, size[1]), max(h, size[0])
        
        if w1 * h1 < w2 * h2:
            w = w1
            h = h1
        else:
            w = w2
            h = h2
        
    return w * h