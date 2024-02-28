import sys
input = sys.stdin.readline
from bisect import bisect_left

n, m = map(int, input().split())

titles = []
nums = []

for _ in range(n):
    a, b = input().split()
    titles.append(a)
    nums.append(int(b))

for _ in range(m):
    print(titles[bisect_left(nums, int(input()))])