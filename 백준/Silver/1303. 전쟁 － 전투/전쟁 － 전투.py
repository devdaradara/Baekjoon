import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(m)]
visited = [[False] * n for _ in range(m)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    que = deque()
    que.append((x, y))
    visited[x][y] = True

    team = graph[x][y]
    num = 1

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if not visited[nx][ny] and graph[nx][ny] == team:
                    num += 1
                    visited[nx][ny] = True
                    que.append((nx, ny))
    return num


blue = 0
white = 0

for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            num = bfs(i, j)
            if graph[i][j] == "B":
                blue += num * num
            else:
                white += num * num

print(white, blue)
