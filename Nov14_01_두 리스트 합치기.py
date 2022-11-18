'''
두 리스트 합치기
오름차순으로 정렬이 된 두 리스트가 주어지면 두 리스트를 오름차순으로 합쳐 출력하는 프로
그램을 작성하세요.
▣ 입력설명
첫 번째 줄에 첫 번째 리스트의 크기 N(1<=N<=100)이 주어집니다.
두 번째 줄에 N개의 리스트 원소가 오름차순으로 주어집니다.
세 번째 줄에 두 번째 리스트의 크기 M(1<=M<=100)이 주어집니다.
네 번째 줄에 M개의 리스트 원소가 오름차순으로 주어집니다.
각 리스트의 원소는 int형 변수의 크기를 넘지 않습니다.
▣ 출력설명
오름차순으로 정렬된 리스트를 출력합니다.
▣ 입력예제 1
3
1 3 5
5
2 3 6 7 9
▣ 출력예제 1
1 2 3 3 5 6 7 9
'''

'''sort로 풀이 -->시간복잡도 때문에 메모리 많이 잡아 먹음 
n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
c=a+b
c.sort()
print(c)
'''
#나의 코드
n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
aIndex=0    #aIndex=bIndex=0 으로 한번에 값을 주는게 낫다
bIndex=0
c=list()    #c=[]가 좋다
while aIndex<n and bIndex<m:
    if a[aIndex]>=b[bIndex]:
        c.append(b[bIndex])
        bIndex+=1
    else:
        c.append(a[aIndex])
        aIndex+=1
    
    #밑에 코드는 while이 끝났을 때를 가정한 코드이므로 while 밖에다 쓰는게 좋음 
    if aIndex==n:
        for i in range(bIndex,m):   #c = c + b[bIndex:]
            c.append(b[i])          #이걸로 한번에 가능 list + list = list를 응용
        
    elif bIndex==m:
        for i in range(aIndex,n):   #c = c + a[aIndex:]
            c.append(a[i])          #이걸로 한번에 가능
for i in c:
    print(i, end=" ")

#해설코드
n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
p1=p2=0
c=[]
while p1<n and p2<m:
    if a[p1]<=b[p2]:
        c.append(a[p1])
        p1+=1
    else:
        c.append(b[p2])
        p2+=1
if p1<n:
    c=c+a[p1:]
if p2<m:
    c=c+b[p2:]

