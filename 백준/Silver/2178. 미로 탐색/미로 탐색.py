import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def bfs(a, b):
    que = deque()
    que.append((a, b))

    while que:
        x, y = que.popleft()

        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if 0 <= xx < n and 0 <= yy < m and graph[xx][yy] == 1:
                que.append((xx, yy))
                graph[xx][yy] = graph[x][y] + 1

bfs(0, 0)
print(graph[n-1][m-1])