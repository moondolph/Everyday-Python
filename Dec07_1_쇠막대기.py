'''
a=list(input().split())
stack=0
sum=0
for i in range(len(a)):
    if a[i]=="(":
        if a[i+1]=="(":
            stack+=1
        else:
            stack-=1
            sum+=stack
    if a[i]==")":
        if a[i+1]=="(":
            stack-=1
            sum+=1
        else:
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
            cnt+=len(stack)
        else:
            stack.pop()
            cnt+=1
print(cnt)