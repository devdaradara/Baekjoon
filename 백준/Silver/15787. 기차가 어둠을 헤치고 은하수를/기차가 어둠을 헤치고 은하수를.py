import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
trains = []

for _ in range(n+1):
    trains.append(deque(["X"] * 20))

for _ in range(m):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        trains[cmd[1]][cmd[2] - 1] = "O"

    elif cmd[0] == 2:
        trains[cmd[1]][cmd[2] - 1] = "X"

    elif cmd[0] == 3:
        trains[cmd[1]].appendleft("X")
        trains[cmd[1]].pop()

    elif cmd[0] == 4:
        trains[cmd[1]].append("X")
        trains[cmd[1]].popleft()

train = []
for i in range(1, n+1):
    if trains[i] not in train:
        train.append(trains[i])

print(len(train))