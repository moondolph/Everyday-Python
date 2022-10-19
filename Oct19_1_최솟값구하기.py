#최솟값 구하기
arr=[5, 3, 7, 9, 2, 5, 2, 6]

##방법1 : 외부에 비교대상 무한대 그릇 만들어 놓고 반복문으로 한번씩 돌려서 가장 작은 값만 저장되도록하기
arrmin=float('inf') #arrmin은 무한대 실수로 외부에 저장해놓고
for i in range(len(arr)):     #배열요소개수만큼 반복문 돌려서 요소 하나하나 비교
    if arr[i]<arrmin:         #arr[i]가 이전 최솟값보다 작으면
        arrmin=arr[i]         #옮겨서 담아
print(arrmin)                 #반복문 끝나고 마지막에 출력

##방법2 : 가장 작은 그릇이 0번째 인덱스 그릇
arrmin2=arr[0]
for i in range(1, len(arr)):
    if arr[i]<arrmin2:
        arrmin2=arr[i]
print(arrmin2)

##방법3 : range 쓸 필요 없고 그냥 바로 배열
arrmin3=float('inf')
for x in arr:
    if x<arrmin3:
        arrmin3 = x
print(arrmin3)


#핵심 : 외부그릇+반복문+조건문