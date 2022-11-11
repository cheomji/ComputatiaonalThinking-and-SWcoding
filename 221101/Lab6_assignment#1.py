#하노이의탑 정리하기... 개어렵ㄴㅔ
def hanoi(n, to_):
    if n == 0:
        return
    
    from_ = findPlace(n)

    if from_ == to_:
        hanoi(n-1, to_)
        return

    aux_ = 6 - from_ - to_

    hanoi(n-1, aux_)
    print(n,': ', from_, ' >> ', to_, sep='')
    move(n, from_, to_)
    global cnt
    cnt += 1
    hanoi(n-1, to_)

def findPlace(n):
    for i in range(3):
        if n in column[i]:
            return i+1

def move(movenum, _from, _to):
    column[_from-1].pop()
    column[_to-1].append(movenum)

column = []
max = 0
cnt = 0
for i in range(3):
    line = [int(item) for item in input().split()]
    column.append(line)
    max += len(line)

hanoi(max, 3)
print(cnt)
