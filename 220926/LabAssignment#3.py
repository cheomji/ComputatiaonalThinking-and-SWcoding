#정수나누기 소수점 100th까지 출력하는 문제
import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
share = a//b
print(share)
for i in range(1, 101):
    a = (a % b)*10
    if a == 0:
        break
    share = a//b
    if i == 100 :
        divnum = (a % b)*10
        check = divnum//b
        if check >= 5:
            print(share+1)
            break
    print(share, end='')
    if i % 10 == 0:
        print()
