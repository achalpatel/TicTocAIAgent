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
    WIN = "win"
    LOSE = "lose"
    DRAW = "draw"
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
    
    def utilityFun(self, board_data, response):
        numberOfSpaceAvail = len(board_data)
        utility = 0
        if response == self.WIN:
            utility += (1 + numberOfSpaceAvail) * (1)
            return utility
        if response == self.LOSE:
            utility += (1 + numberOfSpaceAvail) * (-1)
            return utility
        return utility
        # print("utility - availSpace:",numberOfSpaceAvail)

    def drawEval(self, board_data):
        if len(board_data)<=0:
            return True
        return False

    def minimax(self, letter):
        board_data = self.board.available_space()
        if letter == "X":            
            for val in board_data:                
                self.maxFun(val, board_data.copy())
        elif letter == "O":
            pass
    
    def maxFun(self, pos, board_data):          
        if self.is_winner(self.letter):
            utility = self.utilityFun(board_data, self.WIN)
            return utility
        if self.drawEval(board_data):
            return 0
        availSpaces = board_data
        print("Max-spaces:",availSpaces)
        # self.minFun()
    
    def minFun(self, pos, board_data):
        if self.is_winner(self.letter):
            utility = self.utilityFun(board_data, self.WIN)
            return utility
        if self.drawEval(board_data):
            return 0
                
