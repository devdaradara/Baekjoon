import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pocketmon = {}

for i in range(1, n+1):
    name = input().rstrip()
    pocketmon[i] = name
    pocketmon[name] = i

for _ in range(m):
    question = input().rstrip()
    if question.isdigit():
        print(pocketmon[int(question)])
    else:
        print(pocketmon[question])