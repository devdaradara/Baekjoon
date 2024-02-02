import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    m = int(input())
    nums = list(map(int, input().split()))
    for _ in range(m//10):
        new = list(map(int, input().split()))
        for n in new:
            nums.append(n)

    print(m//2+1)
    idx = 0
    for i in range(m // 2 + 1):
        idx += 1
        new = nums[:2*i+1]
        new.sort()
        print(new[int(len(new)/2)], end=" ")
        if idx % 10 == 0:
            print()
    print()