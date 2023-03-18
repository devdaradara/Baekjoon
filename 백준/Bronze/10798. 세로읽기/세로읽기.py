import sys
input = sys.stdin.readline

letters = [input().rstrip() for _ in range(5)]

for i in range(15):
    for j in range(5):
        try:
            print(letters[j][i], end="")
        except:
            pass
