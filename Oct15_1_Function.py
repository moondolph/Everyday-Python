'''
함수만들기
'''

def add(a,b):
    c=a+b
    print(c)

add(3, 2)
add(5, 7)

def minus(a,b):
    c= a-b
    print(c)

minus(3,5)

def add2(a,b):
    c=a+b
    return c

x=add2(3,4)
print(x)

#return 값 2개 반환도 가능
def add(a,b):
    c=a+b
    d=a-b
    return c, d

print(add(3, 2))

def isPrime(x):             #소수인지 확인하는 Boolean 함수
    for i in range(2, x):   #i는 2부터 x-1까지 루프
        if x%i==0:          #만약 나머지가 0이 되게 하는 숫자가 있으면
            return False    #false를 반환
    return True             #없으면 True를 반환

a=[12, 13, 7, 9, 19]        #여러 숫자들의 리스트가 있는데
for y in a:                 #반복문 돌려서
    if isPrime(y):          #숫자 하나하나를 isPrime함수로 활용가능
        print(y, end=' ')   #조건이 참이면 해당 숫자를 출력







