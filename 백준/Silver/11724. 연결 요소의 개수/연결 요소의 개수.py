import sys
input = sys.stdin.readline

node, edge = map(int, input().split())
graph = [[] for _ in range(node+1)]
visited = [False] * (node + 1)

for i in range(edge):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

stack = []

def dfs(new):
    while stack:
        n = stack.pop()
        if not visited[n]:
            for i in graph[n]:
                stack.append(i)
            visited[n] = True

cnt = 0

for test in range(1, node+1):
    if not visited[test]:
        stack.append(test)
        dfs(test)
        cnt += 1

print(cnt)