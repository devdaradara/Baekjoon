import sys
from operator import itemgetter
n = int(sys.stdin.readline())
human = []

for _ in range(n):
    st = sys.stdin.readline().split()
    name = st[0]
    kor = int(st[1])
    eng = int(st[2])
    math = int(st[3])
    human.append((name, kor, eng, math))

human.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))

for i in range(n):
    print(human[i][0])