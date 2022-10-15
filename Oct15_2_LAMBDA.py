##기존방식-> 함수 만들고 리턴하고 프린트
def plus_one(x):
    return x+1
print(plus_one(1))


##람다함수는 이렇게 할 수 있음
plus_two=lambda x: x+2     #plus_two함수는 람다인데 x를 받아서 x+2를 반환함
print(plus_two(1))         #1을 인수로 받아서 출력

a=[1, 2, 3]                     #map(함수, 리스트)
print(list(map(plus_one,a)))    #a를 받아서 plus_one 자료형으로 바꾼거를
                                # 그대로 list로 담아서 출력
                                #map함수는 람다랑 자주 쓰임

print(list(map(lambda x:x+1,a))) #람다를 활용하면
                                 #a의 자료가 다 x로 들어가서 그대로 list로 저장
                                 #람다로 하면 굳이 plus_one 만들 필요 없지




