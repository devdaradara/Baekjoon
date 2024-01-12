import sys
input = sys.stdin.readline

from collections import deque

people, delete = map(int, input().split())

table = deque()
for i in range(people):
    table.append(i+1)

answer = "<"
cnt = 1
idx = 0

while len(table) != 1:
    if cnt == delete:
        answer += str(table.popleft())
        answer += ", "
        cnt = 1

    else:
        table.append(table.popleft())
        cnt += 1

answer += str(table[0])
answer += ">"
print(answer)