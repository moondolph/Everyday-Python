'''
반복문
'''

a = range(10)
print(list(a))
print(a)
b = range(1,11)
print(list(b))

for i in range(10):
    print(i, end="")

for i in range(10, 0):      #아무 일도 안 일어남
    print(i)                #컴퓨터가 인식을 못함

for b in range(10, 0, -1):    #이렇게 써줘야 1씩 작아지면서 출력
    print(b)

i=1
while i<=10:    #조건
    print(i)    #실행1
    i=i+1       #실행2

i=10
while i>=1:
    print(i)
    i=i-1

i=1
while True:         ##계속 돌아가죠
    print(i)        #i출력
    if(i==5):       #i가 5가 되면
        break       #반복문 종료
    i+=1            #i 1씩 커짐


for i in range(1,11):       #10번 반복하겠다
    print("캬캬캬캬캬컄")


for i in range(1,11):
    if i%2==0:
        continue
        print(i)        #얘는 if의 실행영역이라 continue때문에 발동 안됨

for i in range(1,11):
    if i%2==0:
        continue     #뒤에 그냥 지나가라 ~~!
    print(i)        #얘는 for의 영역이라 continue영향 안 받고 발동 @!


##for-else
for i in range(1,11):
    print(i)
    if i==5:
        break
else:                   #break로 for문 깨져서 작동 안함
    print(11)

for i in range(1,11):
    print(i)
    if i>11:
        break
else:                   #for문 정상적으로 종료되어서 작동함
    print("else작동")


