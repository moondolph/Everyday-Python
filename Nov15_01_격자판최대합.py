n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]

max=0
sum=0

for i in range(n):          #가로와 세로
    sum1=0      #한줄 할 때 마다
    sum2=0      # 그릇 만들어주고
    for j in range(n):
        sum1+=a[i][j]
        sum2+=a[j][i]
    if sum1>max:    #한줄 끝나면 조건문으로 비교
        max=sum1
    if sum2>max:
        max=sum2

sum1=sum2=0
for i in range(n):          #대각선 2개
    sum1 += a[i][i]
    sum2 += a[n-1-i][i]
if sum1 > max:
    max=sum1
if sum2 > max:
    max=sum2
