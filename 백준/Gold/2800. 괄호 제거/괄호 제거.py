import sys
input = sys.stdin.readline
from itertools import combinations

exp = list(input().rstrip())

brackets = []

stack = []
for i in range(len(exp)):
    if exp[i] == "(":
        stack.append(i)
    elif exp[i] == ")":
        brackets.append((stack.pop(), i))

answer = set()

for i in range(len(brackets)):
    for comb in list(combinations(brackets, i+1)):
        tmp = exp[:]
        for idx in comb:
            tmp[idx[0]] = tmp[idx[1]] = ""
        answer.add("".join(tmp))

for item in sorted(list(answer)):
    print(item)