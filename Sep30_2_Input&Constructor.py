#a=input("숫자를 입력하세요 : ")
#print(a)
'''
a,b=10, 20
print(a,b) #1020(x) 10 20 (ㅇ) 이렇게 나옴


a,b = input("숫자를 입력하세요 : ").split() #띄어쓰기로 분리해서 저장
print(a,b)  

a,b = input("숫자를 입력하세요 : ").split(",")  
print(a,b)
print(a+b) #string형이라 붙어서 출력됨
print(type(a))
print(type(a+b))

a=int(a)
print(type(a))

b=int(b)

print(a+b) #이제 나옴
'''
#일일이 int()로 형변환 하기 귀찮으니까

a, b =map(int,input("숫자를 입력하세요 : ").split())  #map을 써서 한번에 해결
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)  #몫
print(a%b)   #나머지  
print(a**b)  #거듭제곱

a=4.3
b=5
c=a+b
print(type(c))  #실수 + 정수 = 실수형

a=2.4
b=2.6
print(type(a+b)) #실수 + 실수 = 실수형(결과값이 정수여도)


