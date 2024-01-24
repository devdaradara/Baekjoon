A=list(map(int,input()))
default="NO"
for i in range(1,len(A)):
    front = 1
    back = 1
    for j in A[:i]:
        front*=j
    for j in A[i:]:
        back*=j
    if(front == back):
        default="YES"
print(default)