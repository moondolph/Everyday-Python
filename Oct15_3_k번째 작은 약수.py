##두 개의 자연수 N과 K가 주어졌을 때, N의 약수들 중 K번째로 작은 수를 출력하는 프로그램
##n, k = int(input().split()) -->이렇게 하면 안되고

n, k = map(int,input().split())         #map을 사용
seq=0
for i in range(1,n+1):
    if n%i ==0:
        seq+=1
    if seq==k:
       print(i)
       break
else:                       #for-else문 : for문에서 break 없을 때 발동하게 하는 것
    print("없음")



