def solution(n, lost, reserve):    
    clothes = [1] * (n+2)
    
    for r in reserve:
        clothes[r] += 1
    for l in lost:
        clothes[l] -= 1
    
    for i in range(1, n+1):
        if clothes[i] == 0:
            if clothes[i - 1] == 2:
                clothes[i - 1] -= 1
                clothes[i] += 1
            elif clothes[i + 1] == 2:
                clothes[i + 1] -= 1
                clothes[i] += 1
    
    cnt = 0
    for i in range(1, n+1):
        if clothes[i] == 0:
            cnt += 1
    
    return n - cnt