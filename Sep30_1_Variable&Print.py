"""변수명짓기
1. 영문, 숫자, _(언더바)로 이루어짐
2. 대소문자 구분
3. 문자 or _로 시작
4. 특수문자 x
5. 파이썬 고유함수명 X ( if, for)
"""
##alt+3 주석
##alt+4 주석 x

#출력 연습


a=1
print(a)  #1 출력
print('-------------')
a=10
print(a)    #10 출력

#2a=5 숫자로 시작해서 안됨
#print(2a)

#값 교환
a, b = 10 , 20
print(a, b) #10 20

a, b = 20 , 10
print(a, b) #20 10

#변수 타입
a=1231252364567451313123123124512
print(a)        

a=12.12353464567547124123123     #실수형은 8바이트(64비트)까지 나옴
print(a)
print(type(a))  #자료형 확인하고 싶을 때

a="student"
print(a)
print(type(a))

#출력방식
print("number")
a, b , c = 1, 2, 3        #여러개 동시에 변수선언 가능
print("number ",a,b,c)
print("number",a,    b,           c)
#sep사용해서  출력되는 모양 컨트롤 가능
print(a,b,c,sep=", ")       #1, 2, 3
print(a,b,c,sep=",")        #1,2,3
print(a,b,c,sep="")         #123
print("----------------")
#줄바꿈
print(a,b,c,sep='\n')       
print("----------------")
print(a)                    #줄바꿔서 프린트하면 출력도 알아서 줄바꿈
print(b)
print(c)
print("----------------")
print(a,end=' ')            #end로 줄 안 바꾸기 가능 
print(b,end='')
print(c,end=' ')
print(a),print(b),print(c)

print(a,b,c)                #줄 안바뀜
print(a),print(b),print(c)  #줄 바뀜 
