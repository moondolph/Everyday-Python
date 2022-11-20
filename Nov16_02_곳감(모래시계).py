n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

for i in range(m):
    b = list(map(int,input().split()))  # 리스트로 받지말고 h, t, k = map(int, input().split())
    if(b[1]==0):
        for j in range(b[2]):
            a[(b[0])-1].append(a[(b[0])-1].pop(0))
    else:
        for j in range(b[2]):
            a[(b[0]) - 1].insert(0,a[(b[0])-1].pop())

s=0
e=n
sum=0
for i in range(n):
    for j in range(s,e):
        sum+=a[i][j]
    if i<n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1
print(sum)





