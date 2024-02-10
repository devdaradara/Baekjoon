import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
machine = list(map(int, input().split()))
machine.sort()
machine = deque(machine)
less = []

if n % 2 == 1:
    less.append(machine.pop())

for _ in range(n//2):
    less.append(machine.pop() + machine.popleft())

print(max(less))