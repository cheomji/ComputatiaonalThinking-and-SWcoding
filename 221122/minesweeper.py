import random

# [출력 형식]
# 빈 칸의 경우 '🔲'로 출력
# 주변 지뢰를 나타내는 수의 경우 ' 1', ' 2'와 같은 형태로 출력
# 깃발의 경우 '🚩'로 출력
# 폭탄의 경우 '💣'로 출력

def installMines(x, y, n):
    '''
	안내) 변수의 이름은 마음대로 변경하여도 좋습니다.
	참고) field: 현재 지뢰밭을 이루는 격자에서, 각 칸 별로 주변의 지뢰가 몇 개가 있는지 저장하는 리스트 (2차원 리스트)
	참고) graphic: 실제 게임을 하는 화면상에서 표시되는 이미지 및 숫자 정보를 저장하는 리스트
	'''
	
    
    temp = ["🔲" for i in range(x)]
    graphic = [temp[:] for i in range(y)]

    tmp = [0 for _ in range(x)]
    field = [tmp[:] for _ in range(y)]
    for _ in range(n):
        while True:
            row = random.randrange(y)
            col = random.randrange(x)
            if field[row][col] != -1:
                field[row][col] = -1
                break

    for i in range(y):
        for j in range(x):
            if field[i][j] == -1:
                if i>0 and j>0 and field[i-1][j-1] != -1:
                    field[i-1][j-1] += 1
                if i>0 and field[i-1][j] != -1:
                    field[i-1][j] += 1
                if i>0 and j<x-1 and field[i-1][j+1] != -1:
                    field[i-1][j+1] += 1
                if j>0 and field[i][j-1] != -1:
                    field[i][j-1] += 1
                if j<x-1 and field[i][j+1] != -1:
                    field[i][j+1] += 1
                if i<y-1 and j>0 and field[i+1][j-1] != -1:
                    field[i+1][j-1] += 1
                if i<y-1 and field[i+1][j] != -1:
                    field[i+1][j] += 1
                if i<y-1 and j<x-1 and field[i+1][j+1] != -1:
                    field[i+1][j+1] += 1
    
    return field, graphic

def currentMap():
    for line in graphic:
        for item in line:
            print(item, end='')
        print()

def findzero(x, y):
    if (-1<y<m and -1<x<n) and mine[y][x] != -1 and (visit[y][x] == False or graphic[y][x] == '🚩'):
        visit[y][x] = True

        if mine[y][x] != 0:
            graphic[y][x] = img[mine[y][x]]
            return
        
        graphic[y][x] = img[0]
        findzero(x-1, y-1)
        findzero(x-1, y)
        findzero(x-1, y+1)
        findzero(x, y-1)
        findzero(x, y+1)
        findzero(x+1, y-1)
        findzero(x+1, y)
        findzero(x+1, y+1)

def touch(x, y, flag):
    if flag == 1:  
        if graphic[y][x] != '🚩':
            graphic[y][x] = '🚩'
            visit[y][x] = True
        else:
            graphic[y][x] = '🔲' # rechanging
            visit[y][x] = False
    else: #flag = 0
        if graphic[y][x] != '🚩':
            if mine[y][x] == -1:
                for _y in range(m):
                    for _x in range(n):
                        if mine[_y][_x] == -1:
                            graphic[_y][_x] = img[-1]
                return False
            else:
                if mine[y][x] != 0:
                    graphic[y][x] = img[mine[y][x]]
                    visit[y][x] = True
                else: #when mine[y][x] is 0
                    findzero(x, y)
                return True

def doeskwin():
    check = True
    for i in range(m):
        for j in range(n):
            if visit[i][j] == False or (graphic[i][j] == '🚩' and mine[i][j] != -1):
                check = False
                break
    return check

mine = []
graphic = []

n, m, k = map(int, input().split())
mine, graphic = installMines(n, m, k) # m : rowsize, n : colsize

temp = [False for _ in range(n)]
visit = [temp[:] for _ in range(m)]
img = [" 0", " 1", " 2", " 3", " 4", " 5", " 6", " 7", " 8", " 9", '💣']

currentMap()
while True:
    _line = input().split()
    x, y, flag = map(int, _line)
    x -= 1
    y -= 1
    game = touch(x, y, flag)
    currentMap()
    if doeskwin() == True:
        print('win!')
        break
    if game == False:
        break
