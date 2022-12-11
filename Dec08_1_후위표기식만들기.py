a=input()
stack=[]
res=''
for x in a:         #입력받은 요소 하나하나에 대하여
    if x.isdecimal():   #숫자면 바로 써버리고
        res+=x
    else:
        if x =='(':     #괄호열기면
            stack.append(x) #바로 스택에 넣고
        elif x =='*' or '/':    # * 또는 /면 
            while stack and (stack[-1]=="*" or stack[-1]=='/'): # 나보다 앞서 있는 stack의 *,/
                res+=stack.pop()        #빼서 넣어주고
            stack.append(x)         #나는 스택에 들어가고
        elif x=='+' or x=='-':      # + 또는 -면 
            while stack and stack[-1] != '(':   # (나올때까지 쌓인 연산자
                res+=stack.pop()                # 다 빼서 결과에 넣고
            stack.append(x)                     # 스택에 + 또는 - 추가하기 
        elif x==')':    #                       # )나오면 
            while stack and stack[-1] !='(':    # (나올때 까지 연산자
                res+=stack.pop()                # 다 빼서 결과에 넣기
            stack.pop()                         # (도 결과에 넣기
while stack:            #마지막으로 남은 연산자들
    res+=stack.pop()    #담아주기
print(res)


#IDEA
#연산자는 다 스택에 담는다
#+,-가 우선순위가 낮으니까 맨 뒤에 가겠지
#*,/는 +, -보다 위에 담긴다 
#(괄호)안에 있는 +,-는 *,/보다 빨리 끄집어 내야함

#3*5*2



