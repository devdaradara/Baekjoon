import sys
n = int(sys.stdin.readline())

stack = []
count = 0
answer = []
cont = True

for i in range(0,n):
    x = int(sys.stdin.readline())

    while count < x :
        count += 1
        stack.append(count)
        answer.append("+")

    if stack[-1] == x:
        stack.pop()
        answer.append("-")

    else:
        cont = False
        print("NO")
        break

if cont:
    for i in range(len(answer)):
        print(answer[i])