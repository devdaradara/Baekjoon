import sys
input = sys.stdin.readline

# 방향 표시
direction = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 해당 방향으로 몇 번?/
move = 1
# 2번 되는지
moving = 0

n = int(input())
find = int(input())
snail = [[0] * n for _ in range(n)]

x = n // 2
y = n // 2
snail[x][y] = 1

current = 0

answer_x = 0
answer_y = 0

for i in range(1, n*n + 1):
    snail[x][y] = i
    if i == find:
        answer_x = x
        answer_y = y
    if current == move:
        moving += 1
        direction += 1
        current = 0
    if moving == 2:
        moving = 0
        move += 1
    x += dx[direction % 4]
    y += dy[direction % 4]
    current += 1

for s in snail:
    for p in s:
        print(p, end=" ")
    print()
print(answer_x + 1, answer_y + 1)
