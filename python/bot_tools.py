import copy

def simulate_turn(player,x,y,board):
	board[y][x][0] += 1
	board[y][x][1] = player 
	#change the board
	def change_board(team_num):
		board_of_change = []
		changed = False
		size = len(board)
		for a in range(size):
			board_of_change_row = []
			for b in range(size):
				board_of_change_row.append(0)
			board_of_change.append(board_of_change_row)
		for a in range(size):
			for b in range(size):
				x = board[a][b][0]
				check_greater = 4
				right = 1
				left  = 1
				up    = 1
				down  = 1
				if a == 0:
					up = 0
					check_greater -= 1
				elif a == size - 1:
					down = 0
					check_greater -= 1
				if b == 0:
					left = 0
					check_greater -= 1
				elif b == size - 1:
					right = 0
					check_greater -= 1
				if x > check_greater:
					changed = True
					board_of_change[a][b] = -1
					if up    == 1:
						if board_of_change[a-1][b] != -1:
							board_of_change[a-1][b] = 1
					if down  == 1:
						if board_of_change[a+1][b] != -1:
							board_of_change[a+1][b] = 1
					if left  == 1:
						if board_of_change[a][b-1] != -1:
							board_of_change[a][b-1] = 1
					if right == 1:
						if board_of_change[a][b+1] != -1:
							board_of_change[a][b+1] = 1
		for a in range(size):
			for b in range(size):
				if board_of_change[a][b] == 1:
					board[a][b][0] += 1
					board[a][b][1] = team_num
				if board_of_change[a][b] == -1:
					board[a][b][0] = 1
		return changed
	while change_board(player):
		1
	return board
def check_points(player,board):
	points = 0
	for a in range(len(board)):
		for b in range(len(board[a])):
			if board[a][b][1] == player:
				points += board[a][b][0]
	return points
def print_board(board):
	os.system('cls' if os.name=='nt' else 'clear')
	for a in range(size):
		sc,s1,s2,s3,s4,s5 = "","","","","",""
		for b in range(size):
			x = board[a][b]
			sc += " -----"
			s1 += "|     "
			s2 += "|" + colors[x[1]] + ["     ","     ","     "," ●   ","  ●  "," ● ● "][x[0]] + end_color
			s3 += "|" + colors[x[1]] + ["     ","  ●  "," ● ● ","   ● "," ● ● ","  ●  "][x[0]] + end_color
			s4 += "|" + colors[x[1]] + ["     ","     ","     "," ●   ","  ●  "," ● ● "][x[0]] + end_color
			s5 += "|     "
		print(sc)
		#print(s1+"|")
		print(s2+"|")
		print(s3+"|")
		print(s4+"|")
		#print(s5+"|")
	print(sc)
def check_move_points(player,x,y,board):
	b = simulate_turn(player,x,y,copy.deepcopy(board))
	return check_points(player,b)