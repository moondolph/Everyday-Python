import heapq as hq
a=[]
while True:
    n=int(input())
    if n==-1:
        break
    if n==0:
        if len(a)==0:
            print(-1)
        else:
            print(-hq.heappop(a))   #출력할 때 -붙이면 됨
    else:
        hq.heappush(a,-n)       #최대힙만들려면 -붙여서 push하면 됨. heappush는 최소힙이 디폴트라...




