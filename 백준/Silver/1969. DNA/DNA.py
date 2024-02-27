import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
dna = [input().rstrip() for _ in range(n)]

types = ["A", "C", "G", "T"]
answer = ""

for i in range(m):
    cnt = [0] * 4
    for d in dna:
        for j in range(4):
            if d[i] == types[j]:
                cnt[j] += 1
    answer += types[cnt.index(max(cnt))]

print(answer)

cnt = 0
for d in dna:
    for i in range(m):
        if d[i] != answer[i]:
            cnt += 1

print(cnt)