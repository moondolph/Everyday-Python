k, n = map(int,input().split())
a=[int(input()) for _ in range(k)]
def Count(length):
    cnt = 0
    for x in Line:
        cnt += (x // length)
    return cnt


#탐색범위지정
lt=0
rt=max(a)

#반복문돌려서 탐색
while lt<=rt:                   #lt가 rt보다 커지면 반복문 깨짐
    mid=(lt+rt)//2
    if Count(mid)>=n:           #Count(mid)함수 : 랜선 길이가 mid일때 만들수 있는 랜선의 개수
        res=mid
        lt=mid+1                #범위 좁히면서 최대 길이의 mid찾기
    else:
        rt=mid-1
print(res)


###########해설코드#############
''' 
def Count(length):
    cnt=0
    for x in Line:
        cnt+=(x//length)
    return cnt


k, n = map(int, input().split())
Line=[]
res=0

# 랜선 길이 탐색을 해야함 --> 범위 지정
# 랜선 길이 범위 = 0 ~ 제일 큰 수
longest=0
for i in range(k):
    tmp=int(input())
    Line.append(tmp)
    longest=max(longest,tmp)
lt=1
rt=longest

#반복문 돌려서 이분탐색
while lt<=rt:                   #lt가 rt보다 커지면 반복문 깨짐
    mid=(lt+rt)//2
    if Count(mid)>=n:           #Count(mid)함수 : 랜선 길이가 mid일때 만들수 있는 랜선의 개수
        res=mid
        lt=mid+1                #범위 좁히면서 최대 길이의 mid찾기
    else:
        rt=mid-1
print(res)
'''
