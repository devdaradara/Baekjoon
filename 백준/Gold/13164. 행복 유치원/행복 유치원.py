import sys
input = sys.stdin.readline

n, k = map(int, input().split())
kids = list(map(int, input().split()))

kids.sort()

diff = [0] * (n-1)

for i in range(n-1):
    diff[i] = kids[i+1] - kids[i]

diff.sort(reverse=True)

print(sum(diff[k-1:]))