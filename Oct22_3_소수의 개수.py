#소수의 개수(에라토스테네스 체)
'''
자연수 N이 입력되면 1부터 N까지의 소수의 개수를 출력하는 프로그램을 작성하세요.
만약 20이 입력되면 1부터 20까지의 소수는 2, 3, 5, 7, 11, 13, 17, 19로 총 8개입니다.
 제한시간은 1초입니다.

▣ 입력설명
첫 줄에 자연수의 개수 N(2<=N<=200,000)이 주어집니다.
▣ 출력설명
첫 줄에 소수의 개수를 출력합니다.
▣ 입력예제 1
20
▣ 출력예제 1
8
'''


n = int(input())
''' 답이 나오긴 하는데 시간 초과로 안됌 --> 모든 숫자를 다 뒤지니까 안됨
discount = 0
for i in range(2,n+1):
    for j in range(2,i):
        if (i % j == 0) :
            discount += 1
            break
print(n-1-discount)
'''

ch=[0]*(n+1) #n+1로 곱해야 인덱스 번호가 n까지 생김 
cnt=0  #소수의 개수 카운트 하는 기능

for i in range(2, n+1): #2부터 n까지 반복문 돌려서
    if ch[i]==0:    #인덱스 값이 0이면 
        cnt+=1      #카운트 해주고
        for j in range(i, n+1, i): #i씩 증가하는 스텝으로 i의 배수들을  
            ch[j]=1  # 다 소수 아닌 거로 처리해 줌.
print(cnt)  #마지막에 cnt만 프린트해주면 소수의 개수만 뽑을 수 있음

'''
i가 2일 때 2 소수 카운트 되고 2, 4, 6, 8, ...다 소수 아님
i가 3일 때 3 소수 카운트 되고 3, 6, 9, 12, ... 다 소수 아님
i가 4일 때 4 소수 카운트 안되고 4, 8, 12, 16, ... 다 소수 아님
i가 5일 때 5 소수 카운트 되고 5, 10, 15, 20, ... 다 소수 아님
i가 6일 때 다 안됨
i가 7일 때 7 소수 카운트 되고 7, 14, 21, 28, ... 다 소수 아님

일단 카운트 하고 나머지 배수들 다 카운트 안되게 처리 했네
'''
