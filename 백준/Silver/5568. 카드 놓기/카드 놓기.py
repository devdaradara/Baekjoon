import sys
input = sys.stdin.readline
from itertools import permutations

n = int(input())
k = int(input())
nums = [input().rstrip() for _ in range(n)]

answer = set()

for per in permutations(nums, k):
    answer.add("".join(per))

print(len(answer))