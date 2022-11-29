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

def currentMap():	# 그래픽 화면을 출력해주는 함수
    for line in graphic:
        for item in line:
            print(item, end='')
        print()

def findzero(x, y):
    #빈 공간 눌렀을 때 주변에 쫙 퍼지게 하는 기능 
    #재귀로 짜도 될 듯. dfs 비슷하게? 전역으로 visit 선언해 놓은거 여기서 쓰는 거인듯...? 아마
    if -1<y<m and -1<x<n and visit[y][x] == False:
        visit[y][x] = True

        if mine[y][x] != 0:
            if mine[y][x] != -1: # 어차피 0 주변인 걸 재귀로 돌렸으니까 그게 지뢰일 일은 없음. 얜 뺴도 될ㄷ듯
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
	# 사용자에게 입력받은 좌표 <x,y>에 대해서,
	# flag = 0은 지뢰찾기 게임에서의 해당 격자 칸을 클릭하는 이벤트, 
	# flag=1값은 오른쪽 마우스를 통해서 깃발을 설치/해제하는 이벤트
	if flag == 1:
		if graphic[y][x] != '🚩':
			graphic[y][x] = '🚩'
		else:
			graphic[y][x] = '🔲' # rechanging
	else:
		if graphic[y][x] != '🚩':
			if mine[y][x] == -1: # 지뢰 있다는 표시가 -1인듯?
				for _y in range(m):
					for _x in range(n):
						if mine[_y][_x] == -1:
							graphic[y][x] = img[-1] # 지뢰 걸렸으면 있던 지뢰 다 보여주고 False값 반환
				return False
			else:
				if mine[y][x] != 0:
					graphic[y][x] = img[mine[y][x]]
				else: #when mine[y][x] is 0
					findzero(x, y)
				return True

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
    if game == False:
        break
