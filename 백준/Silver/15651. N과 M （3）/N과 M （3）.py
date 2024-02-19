import sys
input = sys.stdin.readline

n, m = map(int, input().split())
answer = []


def check():
    if len(answer) == m:
        print(" ".join(map(str, answer)))
        return
    for i in range(1, n+1):
        answer.append(i)
        check()
        answer.pop()


check()