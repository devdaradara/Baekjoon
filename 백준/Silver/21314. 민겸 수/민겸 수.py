import sys
input = sys.stdin.readline

mk = input().rstrip()

M = ""
m = ""
ten = 0

for n in mk:
    if n == "M":
        ten += 1
    # "K"인 경우
    else:
        if ten == 0:
            m += "5"
            M += "5"
        else:
            m += str(10 ** (ten - 1)) + "5"
            M += str(10 ** (ten) * 5)
        ten = 0

    # print("=====")
    # print(n, ten)
    # print(m, M)
if ten > 0:
    m += str(10 ** (ten - 1))
    for _ in range(ten):
        M += "1"

print(M)
print(m)