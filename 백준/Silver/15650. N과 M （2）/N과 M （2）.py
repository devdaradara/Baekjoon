import sys
input = sys.stdin.readline

n, m = map(int, input().split())
answer = []


def check(start):
    if len(answer) == m:
        print(" ".join(map(str, answer)))
        return
    for i in range(start, n+1):
        if i not in answer:
            answer.append(i)
            check(i+1)
            answer.pop()


check(1)