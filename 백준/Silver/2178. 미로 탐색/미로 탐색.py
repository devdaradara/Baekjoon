# import sys
# input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())
maze = [[0] * m for _ in range(n)]
checked = [[False] * m for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


for i in range(n):
    kk = list(input())
    for j in range(m):
        maze[i][j] = int(kk[j])

que = deque()
que.append((0, 0))
checked[0][0] = True

while que:
    new = que.popleft()
    for k in range(4):
        x = new[0] + dx[k]
        y = new[1] + dy[k]
        if x >= 0 and y >= 0 and x < n and y < m:
            if maze[x][y] != 0 and not checked[x][y]:
                checked[x][y] = True
                maze[x][y] = maze[new[0]][new[1]] + 1
                que.append((x, y))

print(maze[n-1][m-1])
