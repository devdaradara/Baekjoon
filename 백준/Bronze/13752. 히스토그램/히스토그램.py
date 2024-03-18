import sys
input = sys.stdin.readline

n = int(input())
array = [int(input()) for _ in range(n)]

for a in array:
    print("=" * a)