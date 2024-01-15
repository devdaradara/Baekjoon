import sys
input = sys.stdin.readline

from math import sqrt

start, end = map(int, input().split())

num = [i for i in range(end + 1)]

num[0] = 0
num[1] = 0

for i in range(2, int(sqrt(end)) + 1):
    if num[i] == 0:
        continue
    for j in range(i + i, end + 1, i):
        num[j] = 0

for i in range(start, end + 1):
    if num[i] != 0:
        print(num[i])