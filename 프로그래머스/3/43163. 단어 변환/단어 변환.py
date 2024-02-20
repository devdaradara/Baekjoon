from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    que = deque()
    que.append((begin, 0))
        
    while que:
        now, cnt = que.popleft()
        if now == target:
            return cnt
            
        for i in range(len(words)):
            diff = 0
            new = words[i]
            for j in range(len(new)):
                if now[j] != new[j]:
                    diff += 1
            if diff == 1:
                que.append((new, cnt+1))
    
    return 0              