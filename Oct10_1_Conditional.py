##if문

x = 7   # = 대입연산자
if x == 7 :             # == 같다연산자
 print("Lucky")
 print("ㅋㅋ")  
   #print("ggg")     들여쓰기 주의


x=5
if x!=7:
    print("ㅎㅎㅎㅎㅎ") 

##중첩if문

x=12
if x>=10:
    if x%2==1:
        print("10이상의 홀수")
    print("10이상의 짝수")


x=10
if x>0:
    if x<10:
        print("10보다 작은 자연수")
    print("0보다 큰 자연수")    
    
x=7
if x>0 and x<10:
    print("10보다 작은 자연수")

x=7
if 0<x<10:      #파이썬 개 좋네 ㄷㄷㄷ
    print("10보다 작은 자연수")

#if분기문
x=10
if x>0:
    print("양수")
else:               #else 위치 확인
    print("음수")


x=93
if x>=90:           #위에서부터 아래로 쫘라라락 여러가지 if중 하나에 걸림              
    print('A')
elif x>=80:         #elif 위치 확인-->if랑 줄 맞춰라
    print('B')
elif x>=70:
    print('C')
elif x>=60:
    print('D')
else: 
    print('F')

#다중 if문
x=93
if x>=90:                       #모든 if에 걸림
    print('A',end=" ")      
if x>=80:
    print('B')
if x>=70:
    print('C')
if x>=60:
    print('D')
if x>=50: 
    print('F')

x=10
if x>5:                         #if에 다 걸려서 print 들여쓰기 노 상관
   print("연 뭐가 나올까?")
if x>3:
        print("gg")

x=9                         #노 상관
if x>5:
    print("5보다 큼")    

if x>8:     
        print("8보다 큼")

x=9                    
if x>5:
    if x<8:                
        print("x는 5보다 크고 8보다 작다")  #얘는 x>5 and x<8 조건일때 발동
    print("x는 5보다 크다")    #얘는 x>5일때 발동하는 영
        print("x는 5보다 크고 8보다 작다") #이렇게 쓰면 에러 뜸 ㅋ 들여쓰기 왔다갔다 하지마셈
   
