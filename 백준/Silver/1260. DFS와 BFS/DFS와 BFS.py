import sys
input = sys.stdin.readline
from collections import deque

node, edge, start = map(int, input().split())
graph = [[] for _ in range(node+1)]

for _ in range(edge):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

stack = []
visitDfs = [False] * (node+1)

def dfs(n):
    if not visitDfs[n]:
        stack.append(n)
        visitDfs[n] = True
        while stack:
            n = stack.pop()
            print(n, end=" ")
            for j in graph[n]:
                dfs(j)

dfs(start)

visitBfs = [False] * (node+1)
print()

que = deque()
def bfs(n):
    if not visitBfs[n]:
        que.append(n)
        visitBfs[n] = True
        while que:
            new = que.popleft()
            print(new, end=" ")
            for i in graph[new]:
                if not visitBfs[i]:
                    visitBfs[i] = True
                    que.append(i)


bfs(start)