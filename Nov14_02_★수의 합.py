'''
수들의 합
N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다. 이 수열의 i번째 수부터 j번째 수까지의
합 A[i]+A[i+1]+…+A[j-1]+A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.
▣ 입력설명
첫째 줄에 N(1≤N≤10,000), M(1≤M≤300,000,000)이 주어진다. 다음 줄에는 A[1], A[2], …,
A[N]이 공백으로 분리되어 주어진다. 각각의 A[x]는 30,000을 넘지 않는 자연수이다.
▣ 출력설명
첫째 줄에 경우의 수를 출력한다.
▣ 입력예제 1
8 3
1 2 1 3 1 1 1 2
▣ 출력예제 1
5
'''

# 내 코드 : 정답은 나오는데 데이터 많아지면 시간초과함 <- n,m이 매우 크다면 불필요한 연산 계속 하니까
'''
n, m = map(int,input().split())
a = list(map(int,input().split()))

cnt=0
sum=0
for i in range(n):
    sum=a[i]
    if sum==m:
        cnt+=1
        continue
    for j in range(i+1,n):
        sum+=a[j]
        if(sum == m):
            cnt+=1
            break
print(cnt)
'''
#해설코드  (인덱스 값이 헷갈려서 이해하는데 시간이 걸렸음)
n, m = map(int,input().split())
a = list(map(int,input().split()))
lt=0
rt=1
tot=a[0]        #tot의 초기값 설정.
cnt=0
while True:
    if tot<m:               #이때 tot는 a[lt] ~ a[rt-1]까지의 합임
        if(rt<n):           #이 rt는 위에 보다 1큼
            tot=tot+a[rt]    #이때 tot는 a[lt] ~ a[rt]까지
            rt+=1
        else:
            break

    elif tot==m:
        cnt+=1
        tot-=a[lt]
        lt+=1

    else:
        tot-=a[lt]
        lt+=1
print(cnt)



#해설--> 나만의 코드 (난 이게 더 직관적이고 이해가 잘 됨)
n, m = map(int,input().split())
a = list(map(int,input().split()))
lt=0
rt=0            #나는 rt를 0부터 시작시킬 것이다
tot=a[0]        #tot의 초기값
cnt=0           #경우의 수 count
while True:
    if tot<m:       #이 tot는 a[lt] ~ a[rt]의 합임
        if(rt<n-1):     #rt가 옆으로 이동하므로 끝을 벗어나는 경우 생각해서 if문 추가
            rt+=1
            tot=tot+a[rt]
        else:
            break
    elif tot==m:
        if(rt<n-1):     #rt가 옆으로 한칸 이동하므로 끝을 벗어나는 경우 생각해서 if문 추가
            cnt+=1
            tot=tot-a[lt]
            lt+=1
            rt+=1
            tot=tot+a[rt]
        else:
            cnt+=1
            break
    else:
        #if(rt<n-1):        안써도 됨. rt를 움직이는게 아니니까
            tot-=a[lt]
            lt+=1
        #else:
        #   tot-=a[lt]
        #   lt+=1

print(cnt)


