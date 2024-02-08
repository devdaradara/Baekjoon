import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
tree = [[] for _ in range(n+1)]
parent = [0] * (n+1)

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def bfs(n):
    que = deque()
    que.append(n)
    parent[n] = 1
    while que:
        now = que.popleft()
        for new in tree[now]:
            if not parent[new]:
                parent[new] = now
                que.append(new)

bfs(1)
for i in range(2, n+1):
    print(parent[i])