'''
반복문을 이용한 문제풀이
1) 1부터 N까지 홀수출력하기
2) 1부터 N까지의 합 구하기
3) N의 약수출력하기
'''

#1) 1부터 N까지 홀수 출력
n = int(input())      #input값은 문자열로 받으므로 int로 바꿔줘야 함
for i in range(1,n+1):
    if(i%2==1):
        print(i,end="")

#2) 1부터 N까지의 합
n = int(input())
sum=0
for i in range(1,n+1):
    sum+=i
print(sum,end="")

#while로 쓴 정답
"""n=int(input())
a=1
sum=0
while a<=n:
    sum+=a
    a+=1
print(sum,end="")"""

#3)N의 약수출력하기
n=int(input())
for i in range(1,n+1):
    if(n%i==0):
        print(i,end=" ")
