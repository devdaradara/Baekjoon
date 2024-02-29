import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))
tree.sort()

start = 1
end = tree[-1]

while start <= end:
    mid = (start + end) // 2

    have = 0
    for t in tree:
        if t - mid > 0:
            have += t - mid

    if have >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)