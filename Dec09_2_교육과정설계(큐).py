from collections import deque

need=input()
dq=deque(need)
n=int(input())
for i in range(n):
    plan=input()
    for x in plan:
        if x in dq:
            if x!=dq.popleft():                 #if문에 있더라도 dq.popleft()는 실행됨 
                print("#%d NO" %(i+1))
                break
    else:
        if len(dq)==0:
            print("#%d YES" %(i+1))
        else:
            print("#%d NO" %(i+1))
        