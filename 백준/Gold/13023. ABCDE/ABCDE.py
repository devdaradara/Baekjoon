import sys
input = sys.stdin.readline

n, m = map(int, input().split())
friends = [[] for _ in range(n+1)]
checked = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

have = False

def isFriend(friend, cnt):
    global have
    if cnt == 5:
        have = True
        return
    checked[friend] = True
    for i in friends[friend]:
        if not checked[i]:
            isFriend(i, cnt + 1)
    checked[friend] = False


for i in range(n):
    isFriend(i, 1)
    if have:
        break
        
if have:
    print(1)
else:
    print(0)

