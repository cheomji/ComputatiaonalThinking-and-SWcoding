def findPosition(row):
	global cnt
	if row == n:
		for i in range(n):
			print(board[i] * ". " + "Q " + (n-board[i]-1) * ". ")
		print()
		cnt += 1
		return
	for i in range(n):
		legal = True
		if i in board:
			legal = False
		for j in range(row-1, -1, -1):
			if (board[j] == i-(row-j)) or (board[j] == i+(row-j)):
				legal = False
				break
		if legal:
			board.append(i)
			findPosition(row+1)
			board.pop()

board = []
n = int(input())
cnt = 0
findPosition(0)
print(cnt)
