import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

x = int(input())

answer = 0


def dfs(node):
    global answer
    if len(graph[node]) == 0:
        return
    for n in graph[node]:
        if not visited[n]:
            answer += 1
            visited[n] = True
            dfs(n)


dfs(x)

print(answer)