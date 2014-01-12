import random, copy
from bot_tools import *

def random_bot(t,val,board):
	#return a random space
	list_of_possible_spaces = []
	for a in range(len(board)):
		for b in range(len(board)):
			if board[a][b][1] in [0,val]:
				list_of_possible_spaces.append([b,a])
	return list_of_possible_spaces[random.randint(0,len(list_of_possible_spaces)-1)]
def easy_bot(t,val,board):
	list_of_possible_spaces = []
	for a in range(len(board)):
		for b in range(len(board)):
			if board[a][b][1] in [0,val]:
				list_of_possible_spaces.append([b,a])
	highest_val = 0
	highest_index = [0,0]
	for a in list_of_possible_spaces:
		#make the change and count how many points we can get
		if check_move_points(t,a[0],a[1],board) > highest_val:
			highest_index = a
	return highest_index
