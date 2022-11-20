a=[list(map(int,input().split())) for _ in range(9)]

def width(a):
    for i in range(9):
        db=[0]*9
        for j in range(9):
            db[(a[i][j]-1)]=1
        if sum(db)!=9:
            return False
    return True

def height(a):
    for i in range(9):
        db=[0]*9
        for j in range(9):
            db[(a[j][i]-1)]=1
        if sum(db)!=9:
            return False
    return True

def box(a):
    for i in range(3):
        for j in range(3):
            db=[0]*9
            for k in range(3):
                for l in range(3):
                    db[a[3*i+k][3*j+l]-1]=1
            if sum(db)!=9:
                return False
    return True

def check(a):
    if width(a) and height(a) and box(a):                   #if all--> if all(조건 for _ in )으로 써야함
        print("YES")
    else:
        print("NO")

############실행창############
check(a)




##################################해설#######################
def check(a):
    for i in range(9):              #가로와 세로
        ch1=[0]*10
        ch2=[0]*10
        for j in range(9):
            ch1[a[i][j]]=1
            ch2[a[j][i]]=1
        if sum(ch1)!=9 or sum(ch2)!=9:
            return False            #중간에 False로 걸리게

    for i in range(3):              #3x3
        for j in range(3):
            ch3=[0]*10
            for k in range(3):
                for s in range(3):
                    ch3[a[3*i+k][3*j+s]]=1
                if sum(ch3)!=9:
                    return False
    return True                    #이상 없으면 마지막에 True





''' 나의 초기 생각
#가로 합 체크
def width_check():
    result=0
    for i in range(9):
        a[i].sort()
        count=0
        for j in range(1,10):
            if(a[i].count(j)==1):
                count+=1
        if count==9:
            result+=1
        else:
            return False
    if result==9:
        return True
    else:
        return False

#세로 합 체크
def height_check():
    result = 0
    for j in range(9):
        b=[]
        for i in range(9):
            b+=a[i][j]
        b.sort()
        count = 0
        for j in range(1, 10):
            if(b.count(j) == 1):
                count += 1
        if count == 9:
            result += 1
        else:
            return False

        if count == 9:
            result += 1
        else:
            return False
    if result == 9:
        return True
    else:
        return False
'''
