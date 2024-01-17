import sys
input = sys.stdin.readline
from collections import deque

def bfs(n):
    que = deque()
    que.append(n)
    visited[n] = True

    while que:
        now = que.popleft()
        for idx, new in enumerate(graph[now]):
            if new and not visited[idx]:
                visited[idx] = True
                que.append(idx)
                
# 초기 설정
n = int(input())
m = int(input())

graph = []
visited = [False] * n

for _ in range(n):
    inp = list(map(int, input().split()))
    graph.append(inp)

trip = list(map(int, input().split()))

# 실행
bfs(trip[0] - 1)

can = True
for t in trip:
    if not visited[t - 1]:
        can = False

if can: print("YES")
else: print("NO")