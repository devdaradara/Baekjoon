import sys
input = sys.stdin.readline

n = int(input())
exp = input().rstrip()
nums = {}

for i in range(n):
    nums[chr(65+i)] = int(input())

stack = []

for e in exp:
    if e.isalpha():
        stack.append(nums[e])
    else:
        second = stack.pop()
        first = stack.pop()
        if e == "*":
            stack.append(first * second)
        elif e == "/":
            stack.append(first / second)
        elif e == "+":
            stack.append(first + second)
        elif e == "-":
            stack.append(first - second)

print("{:.2f}".format(stack[0]))