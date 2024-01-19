import sys
input = sys.stdin.readline

n = int(input())

table = [[0]*2 for _ in range(n)]

for i in range(n):
    start, end = map(int, input().split())
    table[i][0] = end
    table[i][1] = start

table.sort()
cnt = 0
end = -1

for i in range(n):
    if table[i][1] >= end:
        end = table[i][0]
        cnt += 1

print(cnt)

