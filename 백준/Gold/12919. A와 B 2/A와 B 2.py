import sys
input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()
can = False


def make_ab(string):
    global can
    if len(string) == len(s):
        if string == s:
            can = True
            return
        return
    if string[-1] == "A":
        make_ab(string[:len(string)-1])
    if string[0] == "B":
        make_ab(string[1:][::-1])


make_ab(t)

if can:
    print(1)
else:
    print(0)
