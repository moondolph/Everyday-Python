a=[23, 12, 36, 53, 19]
print(a[:3]) #a[0~2] 출력

print(a[1:4])   #a[1~3]출력

print(len(a))   #len(a):리스트의 길이 -> 5가 출력됨

##리스트 출력하기
for i in range(len(a)): # i는 리스트의 요소개수만큼 반복
    print(a[i], end=' ')
print()

##리스트 출력
for x in a:
    print(x, end=' ')
print()

##리스트의 요소중 홀수만 출력
for x in a:
    if x%2==1:
        print(x, end=' ')
print()

## List , Tuple , String 등 여러가지 자료형을 입력받으면 인덱스 값을 포함하는 enumerate객체
for x in enumerate(a):
    print(x)

b=(1, 2, 3, 4, 5)  ##b는 Tuple
print(b[0])     ##b의 0번째 인덱스 값은 1
##b[0]=7  튜플은 덮어쓰기안됨

for x in enumerate(a):
    print(x[0], x[1])
print()

for index, value in enumerate(a):
    print(index,value)
print()

if all(60>x for x in a):    ## all->조건이 다 참이어야 True.  JAVA의 AND
    print("YES")
else:
    print("NO")


if any(15>x for x in a):   ## any->조건 중 하나라도 참이면 True   JAVA의 OR
    print("YES")
else:
    print("NO")


#------------------------------------------------------------------------------

'''
2차원 리스트 생성과 접근
'''

#1차원 리스트 생성
a=[0]*3
print(a)        #[0, 0, 0]

#2차원 리스트 생성
a=[[0]*3 for _ in range(3)]     #_(언더바)로 하면 변수 없이 반복문만 돌음
print(a)    ##[[0, 0, 0], [0, 0, 0], [0, 0, 0]]

a[0][1]=1
print(a)    ##[[0, 1, 0], [0, 0, 0], [0, 0, 0]]

a[1][1]=2
print(a)    ##[[0, 1, 0], [0, 2, 0], [0, 0, 0]]

#2차원 리스트 출력
for x in a:
    print(x)


#2차원 리스트 출력   (위에꺼랑 비교하셈)
for x in a:
    for y in x:
        print(y, end=" ")
    print()




























