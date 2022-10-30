#몇 판 i 선승제 경우의 수 출력하기
def result():
    if lst.count('O') == n:
        for item in lst:
            print(item, end='')
        print()
        global cnt
        cnt += 1
        return

    for i in range(0, 2):
        if lst.count('X') < n:
            lst.append(case[i])
            result()
            lst.pop()

n = int(input())
cnt = 0
case = ['O', 'X']
lst = []
result()
print(cnt)
