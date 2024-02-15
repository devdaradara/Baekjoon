import sys
input = sys.stdin.readline
from collections import deque

n, m, t = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

distance = []

def bfs(a, b):
    que = deque()
    que.append((a, b, 0))
    visited[a][b] = True
    while que:
        x, y, d = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if maze[nx][ny] == 0 and not visited[nx][ny]:
                    que.append((nx, ny, d+1))
                    visited[nx][ny] = True
                elif maze[nx][ny] == 2:
                    distance.append(d + 1 + (n - nx - 1) + (m - ny - 1))
                if nx == n - 1 and ny == m - 1:
                    distance.append(d + 1)

bfs(0, 0)

if len(distance):
    if min(distance) <= t:
        print(min(distance))
    else:
        print("Fail")
else:
    print("Fail")