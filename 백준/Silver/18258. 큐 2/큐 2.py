
from collections import deque
import sys

input = sys.stdin.readline

num = int(input())
que = deque([])

for _ in range(num):
    query = input().split()
    if query[0] == "push":
            que.append(query[1])
    elif query[0] == "pop":
        if len(que):
            print(que.popleft())
        else:
            print(-1)
    elif query[0] == "size":
        print(len(que))
    elif query[0] == "empty":
        if len(que):
            print(0)
        else:
            print(1)
    elif query[0] == "front":
        if len(que):
            print(que[0])
        else:
            print(-1)
    elif query[0] == "back":
        if len(que):
            print(que[-1])
        else:
            print(-1)