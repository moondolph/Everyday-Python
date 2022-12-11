x=input()
y=input()
p=dict()
for i in x:
    #p[i]+=1        #초기값 설정이 안돼 있어서 오류남
    p[i] = p.get(i, 0) + 1
for i in y:
    #p[i]-=1
    p[i] = p.get(i, 0) - 1
    
for value in p.values():
    if value !=0:
        print("NO")
        break
else:
    print("YES")



###해설코드###
'''
a=input()
b=input()
str1=dict()
str=dict()
for x in a:
    str1[x]=str1.get(x, 0) + 1
for x in b:
    str2[x]=str2.get(x, 0) + 1

for i in str1.keys():
    if i in str2.keys():
        if str1[i]!=str2[i]:
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")
'''    


