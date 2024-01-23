import sys
input = sys.stdin.readline
from math import sqrt
from queue import PriorityQueue

num = int(input())
ppi = []

for i in range(num):
    w, h = map(int, input().split())
    now = sqrt(w*w+h*h)/77
    ppi.append([now, i+1])

ppi.sort(key=lambda x:(-x[0], x[1]))

for p in ppi:
    print(p[1])