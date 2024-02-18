import sys
input = sys.stdin.readline
from collections import deque

m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs():
    global last
    que = deque()
    for i in range(n):
        for j in range(m):
            if tomato[i][j] == 1:
                que.append((i, j))
                visited[i][j] = True
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and tomato[nx][ny] == 0 and not visited[nx][ny]:
                que.append((nx, ny))
                tomato[nx][ny] = tomato[x][y] + 1
                visited[nx][ny] = True


bfs()

last = 0
for t in tomato:
    if 0 in t:
        last = 0
        break
    if last < max(t):
        last = max(t)

print(last - 1)