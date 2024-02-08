import sys
input = sys.stdin.readline
from collections import deque

c = int(input())
n = int(input())
coms = [[] for _ in range(c+1)]
visited = [False] * (c+1)

for _ in range(n):
    a, b = map(int, input().split())
    coms[a].append(b)
    coms[b].append(a)

def bfs(n):
    cnt = 0
    que = deque()
    que.append(n)
    visited[n] = True
    while que:
        new = que.popleft()
        for com in coms[new]:
            if not visited[com]:
                que.append(com)
                cnt += 1
                visited[com] = True
    return cnt

print(bfs(1))

