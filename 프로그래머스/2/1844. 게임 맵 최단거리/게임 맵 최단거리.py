from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    def bfs(n, m):
        que = deque()
        que.append((0, 0))

        while que:
            x, y = que.popleft()    
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    que.append((nx, ny))


    bfs(n, m)
    maps[0][0] = 2
    
    if maps[n-1][m-1] == 1:
        return -1
    else:
        return maps[n-1][m-1]
    
    