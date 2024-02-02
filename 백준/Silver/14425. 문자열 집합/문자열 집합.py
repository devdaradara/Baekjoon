import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = []
here = []

for _ in range(n):
    s.append(input().rstrip())

for _ in range(m):
    here.append(input().rstrip())

cnt = 0
for h in here:
    if h in s:
        cnt += 1

print(cnt)