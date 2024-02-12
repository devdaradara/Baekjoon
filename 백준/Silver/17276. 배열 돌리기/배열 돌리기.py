import sys
input = sys.stdin.readline

t = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(t):
    n, degree = map(int, input().split())
    if degree < 0:
        degree += 360
    array = [list(map(int, input().split())) for _ in range(n)]

    for _ in range(degree // 45):
        mid = n // 2

        for r in range(1, n // 2 + 1):
            x = mid - r
            y = mid - r
            direction = -1
            prev = array[x][y]

            for d in range(8):
                if d % 2 == 0:
                    direction += 1
                nx = x + dx[direction] * r
                ny = y + dy[direction] * r
                prev, array[nx][ny] = array[nx][ny], prev
                x = nx
                y = ny

    for a in array:
        for aa in a:
            print(aa, end=" ")
        print()