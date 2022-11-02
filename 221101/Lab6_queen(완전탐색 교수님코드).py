# 완전탐색 버전의 N-Queen
def search(lvl, _x, _y):
	if lvl > n:
		check = True

		for i in range(n):
			for j in range(n):
				if board[i][j] == 'Q':
					# 가로줄 검사
					for x in range(n):
						if x != j and board[i][x] == 'Q':
							check = False
							break
					# 세로줄 검사
					for y in range(n):
						if y != i and board[y][j] == 'Q':
							check = False
							break
					# 대각선 검사
					direction = [[-1,-1],[-1,1],[1,-1],[1,1]]
					for d in direction:
						x = i
						y = j
						while 0 <= d[0] + x < n and 0 <= d[1] + y < n:
							x += d[0]
							y += d[1]
							if board[x][y] == 'Q':
								check = False
								break
				if check == False:
					break
			if check == False:
				break
		
		if check:
			for i in range(n):
				for j in range(n):
					print(board[i][j], end=' ')
				print()
			print()

		return
	
	for x in range(_x, n):
		if x == _x:
			_range = range(_y, n)
		else:
			_range = range(n)
		for y in _range:
			if board[x][y] != 'Q':
				board[x][y] = 'Q'
				search(lvl+1, x, y)
				board[x][y] = '.'

n = int(input("N=? "))
line = ['.' for _ in range(n)]
board = [line[:] for _ in range(n)]

search(1, 0, 0)

