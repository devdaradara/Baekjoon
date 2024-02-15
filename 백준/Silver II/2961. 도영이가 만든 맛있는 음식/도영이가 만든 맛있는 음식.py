import sys
input = sys.stdin.readline

n = int(input())
material = []
total = []

for _ in range(n):
    material.append(list(map(int, input().split())))

def dfs(idx, s, b):
    if idx == n:
        total.append(abs(s - b))
        return
    dfs(idx+1, s, b)
    s *= material[idx][0]
    b += material[idx][1]
    dfs(idx+1, s, b)

if n == 1:
    print(abs(material[0][0] - material[0][1]))
else:
    dfs(0, 1, 0)
    print(min(total[1:]))