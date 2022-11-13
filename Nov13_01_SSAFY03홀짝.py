'''홀짝
N개의 자연수 A[1],A[2],...,A[N]이 주어진다.
또 K개의 자연수 P[1],P[2],...,P[K]가 주어지는데, 이 값들을 순서대로 사용한다.
P[i]를 사용하는 것은 A[1],A[2],...,A[N]들 중 홀수나 짝수를 정해서 모든 홀수나 모든 짝수에 동일한 값 P[i]를 더하는 것이다.
이렇게 해서 전체 합이 최대가 되도록 하고 싶다
만들 수 있는 전체 합의 최대를 제시하라

예제입력)
N = 4, A={2,1,2,2}, K=2, P = {1, 3}

예제결과)
22

예제 풀이)
P[1]=1을 홀수들에 더하면 수열은 {2,2,2,2}로 바뀐다
p[2]=3을 짝수들에 더하면 수열은 {5,5,5,5}로 바뀌고 전체 합은 20이다

P[1]=1을 짝수들에 더하면 수열은 {3,1,3,3}이 되고
P[2]=3을 홀수들에 더하면 수열은 {6,4,6,6}이 되며 이 때 전체 합은 22이고 이 경우가 최대이다.
'''

#나의 코드
#<입력받는 기능>
n=int(input("N = "))
a=list(map(int,input("A = ").split(",")))
k=int(input("K = "))
p=list(map(int,input("P = ").split(",")))

#<a리스트의 홀,짝 개수를 담는 그릇>
a_even = 0
a_odd = 0
#반복문 돌려서 a리스트의 홀/짝 개수 구하기
for i in a:
    if(i % 2 == 0):
        a_even+=1
    else:
        a_odd +=1
#반복문 돌려서 case에 따라 곱하기
cnt=0     #더한 값을 담는 그릇
for i in p:
    if(a_even>a_odd):           #a리스트의 짝수가 더 많을 때
        if(i%2==0):             #p[i]가 짝수일 때
            cnt+=(a_even*i)     #짝수에 더한 값을 cnt에 담는다
        else:                   #p[i]가 홀수일 때
            cnt+=(a_even*i)     #짝수에 더한 값을 cnt에 담는다
            a_odd+=a_even       #홀수+짝수를 했으므로 홀수가 모두 짝수로 변함
            a_even=0            #홀수의 개수는 0이 됨.

    elif(a_even==a_odd):        #a리스트의 짝수 개수와 홀수 개수가 같을 때
        if(i%2==0):
            cnt+=(a_even*i)
        else:
            cnt+=(a_odd*i)
            a_even+=a_odd
            a_odd=0
    else:                       #a리스트의 홀수가 더 많을 때
        if(i%2==0):
            cnt+=(a_odd*i)
        else:
            cnt+=(a_odd*i)
            a_even+=a_odd
            a_odd=0
sum=sum(a)
print(sum+cnt)








