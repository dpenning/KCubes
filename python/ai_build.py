import random, copy
from bot_tools import *

def random_bot(val,board):
	#return a random space
	list_of_possible_spaces = find_all_possible_moves(val,board)
	return list_of_possible_spaces[random.randint(0,len(list_of_possible_spaces)-1)]
def easy_bot(val,board):
	list_of_possible_spaces = find_all_possible_moves(val,board)
	highest_val = 0
	highest_index = [0,0]
	for a in list_of_possible_spaces:
		if check_move_points(val,a[0],a[1],board) > highest_val:
			highest_index = a
	return highest_index
def medium_bot(val,board):
	size = len(board)
	def medium_move_scoring(positions,points):
		if positions == size*size:
			return 1000000
		position_score_coefficient = 10
		points_score_coefficient = 1
		position_score = positions*position_score_coefficient
		points_score = points*points_score_coefficient
		return position_score+points_score
	highest_val = -1
	highest_index = [0,0]
	for a in find_all_possible_moves(val,board):
		if medium_move_scoring(get_board_status_after_move_1_lookahead(vals,a[0],a[1],board)) > highest_val:
			highest_index = a
	return highest_index
