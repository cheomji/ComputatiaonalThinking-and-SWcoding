#가까운 소수 구하기
#입력을 터미널로 해야돼서 입출력처리도 중요함. 근데 함수안써서 너무불편함 코드가;;
import sys
n = int(sys.argv[1])
cnt = 1
while True:
    isPrime1 = True
    isPrime2 = True
    for i in range(2, n-cnt):
        if((n-cnt)%i == 0):
            isPrime1 = False
            break
    for i in range(2, n+cnt):
        if((n+cnt)%i == 0):
            isPrime2 = False
            break
    if isPrime1 == isPrime2 == True:
        print(n-cnt, n+cnt)
        break
    elif isPrime1 == True:
        print(n-cnt)
        break
    elif isPrime2 == True:
        print(n+cnt)
        break
    cnt += 1
