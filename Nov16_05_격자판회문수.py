a = [list(map(int,input().split())) for _ in range(7)]
res=0
for i in range(7):
    for j in range(2,5):
        cnt1=0              #가로 카운트그릇
        cnt2=0              #세로 카운트그릇
        for k in range(0,3):    #a[i][j]기준으로 세번 반복해서 회문 체크하는 기능
            if a[i][j-k]==a[i][j+k]:
                cnt1+=1
            if a[j-k][i]==a[j+k][i]:
                cnt2+=1
        if cnt1==3:         #회문이면 세번 다 통과
            res+=1          #정답 경우의 수 추가
        if cnt2==3:
            res+=1
print(res)


#########해설코드############
board=[list(map(int,input().split())) for _ in range(7)]
cnt=0
for i in range(3):      #비교 시작기준점 잡기
    for j in range(7):  #가로,세로 각각 7번 돌려야하니까
        #가로 회문 비교
        tmp=board[j][i:i+5] #기준점이 위치한 5자리를 리스트에 담아서
        if tmp==tmp[::-1]:  #바로 공식 사용해서 비교가능하니까 리스트활용
            cnt+=1

        #세로 회문 비교
        for k in range(2):
            if board[i+k][j]!=board[i+4-k][j]:
                break           #break걸리면 종료인데
        else:                   #안 걸리면 카운트
            cnt+=1
print(cnt)



#기준점을 어디에 두고 탐색을 시작하느냐
#반복문을 몇 번 돌려야 하는가
#카운트는 어떤 식으로 할 것인가?



