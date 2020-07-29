#----------------------------------------------------------------------------------------
#	Creates and maintain tic-tac-toe board object
#				 
#	(c) 2020 Arjang Fahim
#
#	Date: 7/26/2020
#	email: fahim.arjang@csulb.edu
#   version: 1.0.0
#----------------------------------------------------------------------------------------

from Player.Player import RandomComputerPlayer
from Player.Player import HumanPlayer, SmartPlayer


class Board():

	def __init__(self, board_data):

		self.board_data =  board_data
		self.next_turn = "X"

	def get_game_init_info(self):
		pass


	def get_data(self):
		pass

	def set_data(self, board_data):
		pass

	def available_space(self):
		pass


class TerminalBoard(Board):

	def __init__(self, board_data):
		super().__init__(board_data)
		self.init_game()


	def init_game(self):

		print("Please choose X or O:", end = " ")
		self.h_letter = input()
		if self.h_letter == "x" or self.h_letter == "X":
			self.c_letter = "O"
		else:
			self.c_letter = "X"

		self.draw_board()	
		self.rcp = RandomComputerPlayer(self)
		self.hp = HumanPlayer(self, self.h_letter)
		self.smartPlayer = SmartPlayer(self, self.c_letter)


	def draw_board(self):

		print("\n\n")
		index = 0
		for i in range(3):
			print("\t\t\t  %s | %s  | %s  \n" %(self.board_data[index], self.board_data[index + 1], self.board_data[index + 2]))
			index += 3

	def available_space(self):
		return [i for i, x in enumerate(self.board_data) if x == '-']

	def make_move(self, position):
    	# makes the move and redraw the board on the screen
		self.available_space()


	def is_winner(self, letter, board_list):
		index = 0
		# checking for the row similarity
		for i in range(3):
			
			row_set  = set(board_list[index: index+3])
			if len(row_set) == 1 and (letter in row_set):
				return True
			index +=3

		# checking for the column similarity	
		for i in range(3):
			if (board_list[i] == letter and board_list[i+3] == letter and board_list[i+6] == letter):
				return True	
	
		if (board_list[0] == letter and board_list[4] == letter and board_list[8] == letter):
			return True

		if (board_list[2] == letter and board_list[4] == letter and board_list[6] == letter):
			return True			

		return False 


	def play(self):

		while (len(self.available_space()) != 0): 
			if self.next_turn == "X":
				if self.h_letter == "X":
					self.hp.next_move()	
					self.draw_board()					
					if self.is_winner("X", self.board_data):
						print("X is the winner!")
						exit()
					self.next_turn = "O"
				else:
					# self.rcp.next_move()
					self.smartPlayer.next_move()
					self.draw_board()
					self.smartPlayer.minimax("X")	
					if self.is_winner("X", self.board_data):
						print("X is the winner!")
						exit()
					self.next_turn = "O"
			else:
				if self.h_letter == "O":
					self.hp.next_move()	
					self.draw_board()
					if self.is_winner("O", self.board_data):
						print("O is the winner!")
						exit()
					self.next_turn = "X"
				else:
					# self.rcp.next_move()	
					self.smartPlayer.next_move()
					self.draw_board()
					if self.is_winner("O", self.board_data):
						print("O is the winner!")
						exit()
					self.next_turn = "X"