import sys
input = sys.stdin.readline

exp = input().rstrip()

stack = []
ans = ""
idx = 0

while idx < len(exp):
    e = exp[idx]
    if e == "(":
        stack.append(e)
    elif e == ")":
        while stack and stack[-1] != "(":
            ans += stack.pop()
        stack.pop()
    elif e == "*" or e == "/":
        while stack:
            if stack[-1] == "*" or stack[-1] == "/":
                ans += stack.pop()
            else:
                break
        stack.append(e)
    elif e == "+" or e == "-":
        while stack and stack[-1] != "(":
            ans += stack.pop()
        stack.append(e)
    else:
        ans += e
    idx += 1

while stack:
    ans += stack.pop()

print(ans)