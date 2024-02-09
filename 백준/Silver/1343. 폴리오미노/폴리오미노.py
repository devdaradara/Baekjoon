import sys
input = sys.stdin.readline

board = input().rstrip()

cnt = 0
polio = ""
cant = False

for b in board:
    if b == "X":
        cnt += 1
        if cnt % 4 == 0:
            polio += "AAAA"
            cnt = 0
    else:
        if cnt == 0:
            polio += "."
        elif cnt % 4 == 0:
            polio += "AAAA."
            cnt = 0
        elif cnt % 2 == 0:
            polio += "BB."
            cnt = 0
        else:
            cant = True
            break

# print(cnt)
if cnt == 0:
    print(polio)
elif cnt % 2 == 0:
    polio += "BB"
    print(polio)
elif cant or cnt:
    print(-1)

