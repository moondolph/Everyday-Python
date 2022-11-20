##나의 코드## but, This is not Binary Search
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.append(m)
a.sort()
print(a.index(m)+1)


##
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()    #리스트 정렬
lt=0        #왼쪽 끝 범위 지정
rt=n-1      #오른쪽 끝 범위 지정
while lt<=rt:   #lt가 rt보다 커지면 반복문이 돌지 않는다
    mid=(lt+rt)//2
    if a[mid] == m :
        print(mid+1)
        break
    elif a[mid]< m :
        lt=mid+1
    else:
        rt=mid-1
