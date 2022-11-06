n=int(input())              #좋았다
res=0
for i in range(n):          #반복문 n번 돌린다
    tmp=input().split()     #공백으로 입력받은걸 tmp리스트에 저장
    tmp.sort()              #오름차순 정렬
    a,b,c = map(int,tmp)    #문자열->정수로 매핑
   #3개가 같은 경우
    if a==b and b==c:       #모두 같은 경우부터 체에 걸리게
        money=10000+a*1000
   #2개가 같은 경우
    elif a==b or a==c:
        money=1000+(a*100)
    elif b==c:
        money=1000+(b*100)

    #모두 다른 경우
    else:
        money=c*100
    if money>res:           #상금 제일 큰 애를 res에 담기도록하는 기능
        res=money
print(res)              #마지막에 제일 큰 애 출력
'''    p[i]=list(map(int,input().split()))  #왜 이걸 n번 다 돌린다음 일일이 비교하려고함? -->풀이는 0번째부터 그때그때 비교해 나가야지




#상금을 구하는 함수
def money():

#같은 눈이 세 개가 나오는 경우
    if(a[0]==a[1] and a[1]==a[2]):
        print(10000+(a[0])*1000)

#같은 눈이 두 개가 나오는 경우
    if(a[0]==a[1] and a[0]!=a[2]):
        print(1000+(a[0])*100)
    elif(a[0]==a[2] and a[0]!=a[1]):
        print(1000+(a[0])*100)
    elif(a[1]==a[2] and a[1]!=a[0]):
        print(1000+(a[1])*100)

    #모두 다른 눈이 나오는 경우
    if(a[0]!=a[1] and a[1]!=a[2] and a[2]!=a[0]):
        print(max(a)*100)
'''



