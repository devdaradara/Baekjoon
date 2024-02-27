from collections import deque

def solution(priorities, location):
    que = deque()
    
    for idx, priority in enumerate(priorities):
        que.append((priority, idx))
        
    priorities.sort()
    answer = 1
    
    while que:
        priority, idx = que.popleft()
        
        if priority != priorities[-1]:
            que.append((priority, idx))
            
        else:
            if idx == location:
                return answer
            answer += 1
            priorities.pop()
        