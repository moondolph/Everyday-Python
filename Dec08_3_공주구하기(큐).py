<<<<<<< HEAD
from collections import deque
n, k = map(int,input().split())
dq = list(range(1, n+1))
dq = deque(dq)
while dq:
    for _ in range(k-1):
        cur=dq.popleft()
        dq.append()
    dq.popleft()
    if len(dq)==1:
        print(dq[0])
=======
from collections import deque
n, k = map(int,input().split())
dq = list(range(1, n+1))
dq = deque(dq)
while dq:
    for _ in range(k-1):
        cur=dq.popleft()
        dq.append()
    dq.popleft()
    if len(dq)==1:
        print(dq[0])
>>>>>>> origin/master
        dq.popleft()