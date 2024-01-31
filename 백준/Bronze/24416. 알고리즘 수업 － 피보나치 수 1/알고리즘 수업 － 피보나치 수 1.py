n = int(input())

d = [0] * 100
def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    cnt[0] += 1
    return d[x]

cnt = [0]

print(fibo(n), cnt[0])