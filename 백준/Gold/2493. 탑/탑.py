import sys
input = sys.stdin.readline

n = int(input())
top = list(map(int, input().split()))
laser = [0] * (n+1)
stack = [(0, 0)]

for i in range(n):
    now = top.pop()
    while stack:
        if stack[-1][1] <= now:
            new = stack.pop()
            laser[new[0]] = n - i
        else:
            break
    stack.append((n-i, now))
    # print(i, laser)
    # print(stack)

for idx in range(1, n+1):
    print(laser[idx], end=" ")