import sys
input = sys.stdin.readline

bingo = [list(map(int, input().split())) for _ in range(5)]
nums = [i for _ in range(5) for i in list(map(int, input().split()))]

line = 0
mid = False
cdone = False
ddone = False

for cnt in range(25):
    n = nums[cnt]
    for x in range(5):
        for y in range(5):
            if bingo[x][y] == n:
                bingo[x][y] = 0
                if x == 2 and y == 2:
                    mid = True
                a, b, c, d = 0, 0, 0, 0
                for k in range(5):
                    if bingo[x][k] == 0:
                        a += 1
                    if bingo[k][y] == 0:
                        b += 1
                    if mid:
                        if bingo[k][k] == 0:
                            c += 1
                        if bingo[k][4-k] == 0:
                            d += 1
                if a >= 5:
                    line += 1
                if b >= 5:
                    line += 1
                if c >= 5 and not cdone:
                    line += 1
                    cdone = True
                if d >= 5 and not ddone:
                    line += 1
                    ddone = True

    if line >= 3:
        print(cnt + 1)
        break