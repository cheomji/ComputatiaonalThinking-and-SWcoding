#미완선잉ㅁㅅㅂ 교수님 진도가 너무 빨라요...
def queen(level, _i, _j):
    if level > n:
        check = True
        for i in range(n):
            for j in range(n):
                if board[i][j] == 'Q':
                    #horiz
                    for x in range(n):
                        if x != j:
                            if board[i][x] == 'Q':
                                check = False
                    #vert
                    for y in range(n):
                        if y != i:
                            if board[y][j] == 'Q':
                                check = False
                    #diag
                    direc = [[-1,-1], [-1,1], [1,-1], [1,1]]
                    x = i
                    y = j
                    for di in direc:
                        while (x + di[1])<n and (x + di[i])>=0 :
                            x += 

        for line in board:
            for item in line:
                print(item, end=' ')
            print()
        print()
        return

    for i in range(_i, n):
        for j in range(_j, n):
            if i == _i and j > _j or i > _i:
                if board[i][j] == ".":
                    board[i][j] = 'Q'
                    queen(level+1, i, j)
                    board[i][j] = '.'
        
        queen(level+1)

n = int(input('N=? '))

line = [" " for i in range(n)]
board = [line[:] for i in range(n)]

queen(1)

for line in board:
    print(line)
