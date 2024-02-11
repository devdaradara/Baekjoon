import sys
input = sys.stdin.readline

line = input().rstrip()
answer = ""

bracket = False
tmp = ""

for l in line:
    if l == "<":
        if tmp:
            answer += tmp[::-1]
            tmp = ""
        bracket = True
        tmp += l
    elif l == ">":
        bracket = False
        answer += tmp + ">"
        tmp = ""
    elif l == " " and not bracket:
        answer += tmp[::-1] + " "
        tmp = ""
    else:
        tmp += l
    # print(l, answer, tmp)

if not bracket:
    answer += tmp[::-1]

print(answer)