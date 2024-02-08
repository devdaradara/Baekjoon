import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
nums = []

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def bfs(a, b):
    cnt = 1
    que = deque()
    graph[a][b] = 0
    que.append((a, b))
    while que:
        x, y = que.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < n and graph[xx][yy] == 1:
                graph[xx][yy] = 0
                que.append((xx, yy))
                cnt += 1
    return cnt

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            count = bfs(i, j)
            nums.append(count)

nums.sort()
print(len(nums))
for a in nums:
    print(a)