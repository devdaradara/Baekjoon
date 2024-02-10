import sys
input = sys.stdin.readline

a, b = map(int, input().split())

cnt = 0
while b > a:
    cnt += 1
    if b % 2:
        if str(b)[-1] != "1":
            break
        b = int(str(b)[:len(str(b))-1])
    else:
        b = b // 2

if a == b:
    print(cnt + 1)
else:
    print(-1)