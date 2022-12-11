a=input()
stack=[]
for x in a:
    if x.isdecimal():
        stack.append(int(x))
    else:
        if x=="+":
            nb=stack.pop()
            nf=stack.pop()
            stack.append(nf+nb)
        elif x=="-":
            nb=stack.pop()
            nf=stack.pop()
            stack.append(nf-nb)
        elif x=="*":
            nb=stack.pop()
            nf=stack.pop()
            stack.append(nf*nb)
        else:
            nb=stack.pop()
            nf=stack.pop()
            stack.append(nf/nb)
print(stack[0])


#IDEA
#숫자는 스택으로
#연산자는 자기 앞에 두 숫자 계산하고 결과값을 다시 스택으로
#반복
#마지막엔 스택에 숫자 하나가 남는다

