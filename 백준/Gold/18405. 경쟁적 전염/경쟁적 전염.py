import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
s_final, x_final, y_final = map(int, input().split())

virus = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            virus.append((graph[i][j], i, j))
virus.sort()


def bfs():
    que = deque()
    for t, x, y in virus:
        que.append((t, x, y, 0))

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while que:
        t, x, y, s = que.popleft()
        if s == s_final:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = t
                que.append((t, nx, ny, s+1))


bfs()
print(graph[x_final-1][y_final-1])
