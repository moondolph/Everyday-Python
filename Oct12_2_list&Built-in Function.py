import random as r      #이런식으로 객체 불러옴
                        #자바에서는 random r = new random(); 이렇게 했었는데 ..
a1=50
a2=70
a3=80
##ㄴ이런식으로 일일이 변수만들면 불편함

a=[50,70,80] #List로 한번에 바로 만들 수 있다

a=[]        #List만드는법 1
print(a)    #빈리스트 출력

b=list()    #List만드는법 2

a=[1, 2, 3, 4, 5]
print(a)
print(a[0])
print(a[1])

b=list(range(1, 11))
#print(b)

c=a+b   #리스트끼리 합치기 가능
#print(c)

print(a)
a.append(6) #a라는 리스트에 6 추가
print(a)

a.insert(3,7)   #a 리스트의 3번 자리에 7 삽입
print(a)

a.pop() #리스트에서 맨뒤에 인덱스 뺌
print(a)
a.pop(3) #3번자리 ㄲㅈ~!
print(a)

a.remove(4) #리스트에서 숫자 4 제거
print(a)

print(a.index(5))


a=list(range(1,11))
print(a)
print(sum(a))   #a 리스트의 합
print(max(a))   #a 리스트의 최대값
print(min(a))   #a 리스트의 최소값
print(min(7,3,5))  #7,3,5중 최소값

print(a)


r.shuffle(a)   #a를 랜덤으로 섞어
print(a)

a.sort()    #a를 오름차순으로 정렬
print(a)

a.sort(reverse=True) #a를 내림차순으로 정렬
print(a)

a.clear()   #a 리스트 다 없애
print(a)





