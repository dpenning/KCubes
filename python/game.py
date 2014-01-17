import sys, os, time, random, copy, ai_build

end_color = "\033[0m"
colors = ["\033[0;37m","\033[0;31m","\033[0;34m","\033[0;32m","\033[0;33m"]

size = 5
players = 4
player_type_list = ["Human","Medium","Easy","Easy"]
move_time = .5

if '-size' in sys.argv:
	size_position = sys.argv.index('-size') + 1
	if size_position != len(sys.argv):
		size = sys.argv[size_position]
		if size < 2:
			size = 4
if '-players' in sys.argv:
	players_position = sys.argv.index('-players') + 1
	if players_position != len(sys.argv):
		players = int(sys.argv[players_position])
print("Size of Board :",size)
print("Num of Players:",players)

all_players = [x for x in range(1,players+1)]

#initialize
board = []
for a in range(size):
	l = []
	for b in range(size):
		l.append([1,0])
	board.append(l)
players_left_list = all_players[:]
for a in range(players):
	players_left_list[a] = [players_left_list[a],player_type_list[a]]
		
#check if game is over
def players_left():
	on_board = []
	for a in board:
		for b in a:
			if b[1] not in on_board:
				on_board.append(b[1])
	if 0 in on_board:
		return all_players
	return on_board

#print the board
def print_board():
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

#change the board
def change_board(team_num):
	board_of_change = []
	changed = False
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

#check if a player is still on the board
def check_if_player_left(player_number):
	x = players_left()
	if player_number in x:
		return True
	return False

#AI functions
def ai_handout_function(t,val):
	bc = copy.deepcopy(board)
	if t == 'Medium':
		return medium_bot(val,bc)
	if t == 'Easy':
		return easy_bot(val,bc)
	if t == 'Random':
		return random_bot(val,bc)
	else:
		return easy_bot(val,bc)

def random_bot(val,board_copy):
	return ai_build.random_bot(val,board_copy)
def easy_bot(val,board_copy):
	return ai_build.easy_bot(val,board_copy)
def medium_bot(val,board_copy):
	return ai_build.easy_bot(val,board_copy)

#winnning screen
def winner(num):
	os.system('cls' if os.name=='nt' else 'clear')
	print("Winner is ",num)

#write log
def insert_into_log(log,player_val,x,y):
	#insert
	log.write(str(player_val) + "\t" + str(x) + "\t" + str(y) + "\n")

def play_game():
	# this is the gamestate
	log = open('logs/' + time.strftime("%H:%M_%m-%d-%Y") + '.txt','w')
	while True:
		current_player = players_left_list.pop(0)
		current_player_val = current_player[0]
		current_player_type = current_player[1]
		if len(players_left_list) == 0:
			break
		if check_if_player_left(current_player_val):
			print_board()
			if current_player_type == "Human":
				while True:
					print(players_left_list)
					move = input("Player " + str(current_player_val) + " X,Y Position for move: ")
					if len(move.split(',')) == 2:
						x,y = move.split(',')
					else:
						continue
					if x.isdigit() and y.isdigit():
						x = int(x)
						y = int(y)
					else:
						continue
					if board[y][x][1] in [0,current_player_val]:
						board[y][x][1] = current_player_val
						board[y][x][0] += 1
						break
					else:
						continue
			else:
				x,y = ai_handout_function(current_player_type,current_player_val)
				if board[y][x][1] in [0,current_player_val]:
					board[y][x][1] = current_player_val
					board[y][x][0] += 1
			insert_into_log(log,current_player_val,x,y)
			print_board()
			while change_board(current_player_val):
				time.sleep(move_time)
				print_board()
			#put them back in the list of players
			players_left_list.append(current_player)
		else:
			if len(players_left()) == 1:
				print("""
					+-----------+
					| GAME OVER |
					+-----------+""")
	winner(current_player)
	log.close()


if __name__ == "__main__":
	play_game()