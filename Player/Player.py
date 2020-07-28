#----------------------------------------------------------------------------------------
#   Player object contains different kind of players
#                
#   (c) 2020 Arjang Fahim
#
#   Date: 7/26/2020
#   email: fahim.arjang@csulb.edu
#   version: 1.0.0
#----------------------------------------------------------------------------------------


import math
import random

class Player():
    def __init__(self, board):
        self.board = board

class RandomComputerPlayer(Player):
    def __init__(self, board):
        super().__init__(board)
        
    
    def next_move(self):
        available_space = self.board.available_space()
        
        square = random.choice(available_space)
        self.board.board_data[square] = self.board.c_letter


class HumanPlayer(Player):
    def __init__(self, board, letter):
        super().__init__(board)
        self.letter = letter
        print("human letter",self.letter)

    def next_move(self):
        print ("Please enter your move ", end = " ")
        square = input()
        self.board.board_data[int(square)-1] = self.board.h_letter
        
class SmartPlayer(Player):
    def __init__(self, board, letter):
        super().__init__(board)
        self.letter = letter
        print("smart letter",self.letter)

    def next_move(self):
        avail_space = self.board.available_space()
        print("availspace from nextMove:",avail_space)

    def is_winner(self, letter):
        return self.board.is_winner(letter)
                    
    def available_moves(self):
        self.availMoves = self.board.available_space()

    def minimax(self, letter):
        if letter == "X":
            pass
        elif letter == "O":
            pass
    
    def maxFun(self, pos, board):
        pass        
        # if self.is_winner(self.letter)
