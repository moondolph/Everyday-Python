msg="It is Time"
print(msg.upper())
print(msg.lower())
print(msg)

tmp=msg.upper()
print(tmp)
print(tmp.find('T'))
print(tmp.count('T'))

print(msg[:2])      #0번부터 1번
print(msg[3:5])     #3,4번 인덱스만

print(len(msg))     #문자열길이(공백포함)

for i in range(len(msg)):
    print(msg[i], end=' ')
print()


for x in msg:
    print(x, end=' ')
print()

for x in msg:
    if x.isupper():   #만약 x가 대문자면
        print(x, end=" ")      # x출력
print()

for x in msg:
    if x.islower():
        print(x, end=" ")
print()

for x in msg:
    if x.isalpha(): #만약 x가 알파벳이면
        print(x, end='')   #x출력
print()

tmp='AZ'
for x in tmp:
    print(ord(x))   #x의 아스키넘버 출력

tmp='az'
for x in tmp:
    print(ord(x))   #x의 아스키넘버 출력








