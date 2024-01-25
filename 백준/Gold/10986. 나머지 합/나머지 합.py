import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
sums = []
reminds = [0] * m

tmp = 0
for i in nums:
    tmp += i
    reminds[tmp % m] += 1

cnt = reminds[0]

for i in reminds:
    cnt += i * (i-1) // 2

print(cnt)