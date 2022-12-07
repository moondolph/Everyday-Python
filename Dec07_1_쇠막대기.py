'''얘는 조건 비교후 값을 저장해야하는데 얘는 순서의 일관성이 없다 
a=list(input())
stack=0
sum=0
for i in range(len(a)):
    if a[i]=="(":
        if a[i+1]=="(":
            stack+=1
        else:
            sum+=stack
    else:
        if a[i+1]==")":
            stack-=1
            sum+=1
print(sum)
'''


s=input()
stack=[]
cnt=0
for i in range(len(s)):
    if s[i]=='(':
        stack.append(s[i])
    else:
        #stack.pop()<-- 밑에 중복되니까 여기다 써도 됨
        if s[i-1]=='(':         
            stack.pop()
            cnt+=len(stack) #stack에 담겨있는 '(' 의 개수만큼 레이저 맞았을때 더해줌
        else:
            stack.pop()
            cnt+=1
print(cnt)


''' 처음부터 stack은 '('를 담는 개수 
a=list(input())
stack=0
sum=0
for i in range(len(a)):
    if a[i]=="(":
        stack+=1
        if a[i+1]==")":
            stack-=1

    else:
        if a[i-1]=="(":
            sum+=stack
        else:
            stack-=1
            sum+=1
print(sum)
'''