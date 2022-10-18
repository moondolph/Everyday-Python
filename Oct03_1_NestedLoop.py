for i in range(5):
    for j in range(5):
        print(j, end=' ')
    print()

for i in range(5):
    print('i:', i, sep='', end=' ')         #sep='' 이렇게 하면 딱 붙어서 나옴
    for j in range(5):
        print('j:', j, sep='', end=' ')
    print()

for i in range(5):
    for j in range(5):
        print("*", end=' ')
    print()     #줄바꿈

print("줄바꿈 기능"),print()
print("공백 이구나")

#별찍기 예제
"""
*
**
***
****
*****
"""
for i in range(5):
    for j in range(i+1):
        print("*",end="")
    print()


print("---------------------")

"""
*****
****
***
**
*
"""
for i in range(5):
    for j in range(5-i):
        print("*",end="")
    print()

#역시 문제를 풀어야 실력이 늘음.
##문제 풀면서 많이 쳐라







