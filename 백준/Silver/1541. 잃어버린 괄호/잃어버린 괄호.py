import sys
input = sys.stdin.readline

exp = input().rstrip()

answer = 0

num = ""
tmp = 0
minus = False

for e in exp:
    if e == "+":
        tmp += int(num)
        num = ""
    elif e == "-":
        tmp += int(num)
        if minus:
            answer -= tmp
        else:
            answer += tmp
        num = ""
        tmp = 0
        minus = True
    else:
        num += e

tmp += int(num)
if minus:
    answer -= tmp
else:
    answer += tmp
print(answer)