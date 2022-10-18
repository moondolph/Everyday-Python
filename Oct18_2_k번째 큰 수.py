n, k = map(int,input().split())
a = list(map(int,input().split()))
res=set()   #res는 set이라는 자료구조가 되어 중복을 제거한
         
for i in range(n):
    for j in range(i+1, n):
         for m in range(j+1, n):
             res.add(a[i]+a[j]+a[m])
res=list(res)   #set은 sort기능이 없어서 list로 바꿔줌
res.sort(reverse=True)  #내림차순정렬
print(res[k-1]) #k번째 수 출력

