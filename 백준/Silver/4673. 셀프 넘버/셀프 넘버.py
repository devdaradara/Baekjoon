numbers = list(range(1, 10001))
removes = []
for num in numbers :
    for n in str(num):
        num += int(n)
    if num <= 10000:
        removes.append(num)

for re_num in set(removes):
    numbers.remove(re_num)
for num in numbers:
    print(num)