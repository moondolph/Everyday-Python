'''가장 큰 수
선생님은 현수에게 숫자 하나를 주고, 해당 숫자의 자릿수들 중 m개의 숫자를 제거하
여 가장 큰 수를 만들라고 했습니다. 여러분이 현수를 도와주세요.(단 숫자의 순서는
유지해야 합니다)
만약 5276823 이 주어지고 3개의 자릿수를 제거한다면
7823이 가장 큰 숫자가 됩니다.
▣ 입력설명
첫째 줄에 숫자(길이는 1000을 넘지 않습니다)와 제가해야할 자릿수의 개수가 주어집니다.
▣ 출력설명
가장 큰 수를 출력합니다.
▣ 입력예제 1
5276823 3
▣ 출력예제 1
7823
▣ 입력예제 2
9977252641 5
▣ 출력예제 2
99776
'''

#자기 보다 작은 수가 앞에 있으면 지워버린다. 
#스택 : LIFO(Last In First Out) --> 리스트로 풀이


num, m = map(int, input().split())
num=list(map(int,str(num))) #숫자를 하나씩 뜯어서 리스트에 담기
stack=[]                    #스택 생성
for x in num:               #숫자 하나하나에 대하여
    while stack and m>0 and stack[-1]<x:    # 만약 stack에 값이 있고,
                                            # 아직 더 제거할 수 있고,
                                            # stack의 마지막 값이 x보다 작으면
        stack.pop()     # stack의 마지막 값 제거
        m-=1            # 제거 했으니까 카운트 감소
    stack.append(x)     # 더 이상 제거할 수 없으면 stack에 x를 추가         

if m!=0:                # 다 돌리고 보니까 아직 제거횟수가 남았음
    stack=stack[:-m]    # 끝 부분 잘라버리기
print(stack)

res=''.join(map(str,stack))             #for문 안쓰고 join으로 가능 
print(res)

'''        #for 반복문으로 print 가능
for x in stack:
    print(x, end='')
'''

