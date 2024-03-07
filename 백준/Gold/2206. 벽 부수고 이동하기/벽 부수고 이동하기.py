import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]


def bfs():
    que = deque()
    que.append((0, 0, 1))
    graph[0][0] = 1
    visited[0][0][1] = 1

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while que:
        x, y, broke = que.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][broke]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0 and not visited[nx][ny][broke]:
                    que.append((nx, ny, broke))
                    visited[nx][ny][broke] = visited[x][y][broke] + 1
                if graph[nx][ny] == 1 and broke == 1:
                    que.append((nx, ny, broke - 1))
                    visited[nx][ny][broke - 1] = visited[x][y][broke] + 1
    return -1


print(bfs())