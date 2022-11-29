'''
증가수열 만들기(그리디)
1부터 N까지의 모든 자연수로 구성된 길이 N의 수열이 주어집니다.
이 수열의 왼쪽 맨 끝 숫자 또는 오른쪽 맨 끝 숫자 중 하나를 가져와 나열하여 가장 긴 증가수열
을 만듭니다. 이때 수열에서 가져온 숫자(왼쪽 맨 끝 또는 오른쪽 맨 끝)는 그 수열에서 제거됩니
다.
예를 들어 2 4 5 1 3 이 주어지면 만들 수 있는 가장 긴 증가수열의 길이는 4입니다.
맨 처음 왼쪽 끝에서 2를 가져오고, 그 다음 오른쪽 끝에서 3을 가져오고, 왼쪽 끝에서 4,
왼쪽 끝에서 5를 가져와 2 3 4 5 증가수열을 만들 수 있습니다.
▣ 입력설명
첫째 줄에 자연수 N(3<=N<=100)이 주어집니다.
두 번째 줄에 N개로 구성된 수열이 주어집니다.
▣ 출력설명
첫째 줄에 최대 증가수열의 길이를 출력합니다.
두 번째 줄에 가져간 순서대로 왼쪽 끝에서 가져갔으면 ‘L', 오른쪽 끝에서 가져갔으면 ’R'를 써
간 문자열을 출력합니다.(단 마지막에 남은 값은 왼쪽 끝으로 생각합니다.)
▣ 입력예제 1
5
2 4 5 1 3
▣ 출력예제 1
4
LRLL
▣ 입력예제 2
10
3 2 10 1 5 4 7 8 9 6
▣ 출력예제 2
3
LRR
'''
''' 나의 아이디어
n = int(input())
a = list(map(int,input().split()))
max=0
len=0
letter=[]

while True:                 
    if a[-1]>a[0]>max:      #이 방식으로하면 max보다 하나만 큰 경우는 처리할 수 없다
        max=a[0]                --> if - if로 하고 담은 다음 정렬 
        a.pop(0)
        len+=1
        letter.append("L")
    elif a[0]>a[-1]>max:
        max=a[-1]
        a.pop()
        len+=1
        letter.append("R")
    else:
        break
print(len)

for i in letter:
    print(i)
'''
#해설코드
n=int(input())
a=list(map(int,input().split()))

#초기화
lt=0
rt=n-1
last=0      #제일 큰거
res=""      #문자열
tmp=[]      #두 개 넣어서 정렬할 빈 리스트

while lt<=rt:
    if a[lt]>last:
        tmp.append((a[lt], "L"))
    if a[rt]>last:
        tmp.append((a[rt], "R"))
    tmp.sort()
    if len(tmp)==0:
        break
    else:
        res=res+tmp[0][1]
        last=tmp[0][0]
        if tmp[0][1] == 'L' :
            lt+=1
        else:
            rt-=1
    tmp.clear()     #싹 지워버림
print(len(res))
print(res)



