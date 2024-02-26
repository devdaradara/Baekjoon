import sys
input = sys.stdin.readline
from itertools import combinations

n, m = map(int, input().split())
likes = [list(map(int, input().split())) for _ in range(n)]

max_sum = 0
for a, b, c in list(combinations(range(m), 3)):
    tmp = 0
    for i in range(n):
        tmp += max(likes[i][a], likes[i][b], likes[i][c])
    max_sum = max(tmp, max_sum)
    
print(max_sum)