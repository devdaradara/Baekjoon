import sys
input = sys.stdin.readline

bracket = input().rstrip()
stack = []
metal = 0

for i in range(len(bracket)):
    if bracket[i] == "(":
        stack.append("(")
    else:
        stack.pop()
        if bracket[i-1] == "(":
            metal += len(stack)
        else:
            metal += 1

print(metal)