def solution(sizes):    
    w = 0
    h = 0
    
    for s in sizes:
        s.sort()
            
    for i in range(len(sizes)):
        w = max(w, sizes[i][0])
        h = max(h, sizes[i][1])
    
    return w*h