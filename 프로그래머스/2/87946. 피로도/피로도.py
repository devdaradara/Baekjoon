answer = 0

def check(piro, cnt, visited, dungeons):
    global answer
    if cnt > answer:
        answer = cnt            
        
    for i in range(len(dungeons)):
        if not visited[i] and piro >= dungeons[i][0]:
            visited[i] = True
            check(piro - dungeons[i][1], cnt + 1, visited, dungeons)
            visited[i] = False


def solution(k, dungeons):
    global asnwer
    dungeons.sort(reverse=True)
    visited = [False] * len(dungeons)
           
        
    check(k, 0, visited, dungeons)
    
    return answer