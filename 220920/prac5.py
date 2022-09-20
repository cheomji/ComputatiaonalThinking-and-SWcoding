#제어문 배운 날. 근데 입력 이거 교수님은 다르게 받던디;
#그리고 5개씩 출력하는거 어케하는지 모르겠음 ㅅㅂ
s = int(input('start > '))
e = int(input('end > '))
n = int(input('sum > '))
cnt = 0
for i in range(10000, 1000000):
    num = [i//10000, i%10000//1000, i%10000%1000//100, i%10000%1000%100//10, i%10]
    check = True
    for j in range(0, 5):
        if num[j] not in range(s, e+1):
            check = False
            break
    if check == True:
        if num[0]+num[1]+num[2]+num[3]+num[4] == n:
            print(num[0], num[1], num[2], num[3], num[4], sep='')
            cnt += 1
            if cnt != 0 and cnt % 5 == 0:
                print()
if cnt == 0:
    print('No answer')
