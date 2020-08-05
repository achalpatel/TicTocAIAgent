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
        self.opp_letter = ""
        if self.letter == "X":
            self.opp_letter = "O"
        else:
            self.opp_letter = "X"
        print("smart letter",self.letter)

    def next_move(self):
        # avail_space = self.board.available_space()
        # print("availspace from nextMove:",avail_space)
        ans = self.minimax(self.letter)
        self.board.board_data[ans] = self.letter


    def is_winner(self, letter, board_list):
        return self.board.is_winner(letter, board_list)

    def is_opponent_winner(self, board_list):
        return self.board.is_winner(self.opp_letter, board_list)

    def available_moves(self):
        self.availMoves = self.board.available_space()
    
    def available_space_player(self, board_list):
        return [i for i, x in enumerate(board_list) if x == '-']

    def utilityFun(self, board_free_space, response):
        numberOfSpaceAvail = len(board_free_space)
        utility = 0
        if response == self.WIN:
            utility = (1 + numberOfSpaceAvail) * (1)
            # print("utility",numberOfSpaceAvail, utility)
            return utility
        elif response == self.LOSE:
            utility = (1 + numberOfSpaceAvail) * (-1)
            # print("utility",numberOfSpaceAvail, utility)
            return utility
        return utility
        # print("utility - availSpace:",numberOfSpaceAvail)

    def drawEval(self, board_free_space, board_list):
        if not (self.is_winner(self.letter, board_list) or self.is_opponent_winner(board_list)) and len(board_free_space)<=0:
            return True
        return False

    def findMin(self, l):
        mink=math.inf
        boardk = []
        for d in l:
            for x,y in d.items():
                if x<mink:
                    mink=x
                    boardk=y
        ans = {mink:boardk}
        return ans
    
    def findMax(self, l):
        maxk=-math.inf
        boardk = []
        for d in l:
            for x,y in d.items():
                if x>maxk:
                    maxk=x
                    boardk=y
        ans = {maxk:boardk}
        return ans

    def minimax(self, letter):
        board_free_space = self.board.available_space()        
        board_list = self.board.board_data.copy()
        print("Free space:",board_free_space)
        print("Board lIst: ", board_list)
        if letter == "X":
            l = []
            local_dict = {}
            for val in board_free_space:                
                ans_dict = self.maxFun(val, board_list.copy())
                l.append(ans_dict)
                for k in ans_dict.keys():
                    local_dict[k] = val
            ans = self.findMax(l)
            print(ans)
            key_val=0
            for k in ans.keys():
                key_val=local_dict[k]
                print(key_val)
            return key_val

        elif letter == "O":
            l = []
            local_dict = {}
            for val in board_free_space:                
                ans_dict = self.minFun(val, board_list.copy())
                l.append(ans_dict)
                for k in ans_dict.keys():
                    local_dict[k] = val
            ans = self.findMin(l)
            print(ans)
            key_val=0
            for k in ans.keys():
                key_val=local_dict[k]
                print(key_val)
            return key_val
    
    def maxFun(self, pos, board_list):          
        board_list[pos] = self.letter
        board_free_space = self.available_space_player(board_list)
        print("Max",board_list,board_free_space)
        if self.is_winner(self.letter, board_list):
            utility = self.utilityFun(board_free_space, self.WIN)
            # print("W:",utility)
            return {utility:board_list}
        if self.is_opponent_winner(board_list):
            utility = self.utilityFun(board_free_space, self.LOSE)
            # print("L:",utility)
            return {utility:board_list}
        if self.drawEval(board_free_space, board_list):
            return {0:board_list}                
        l = []
        
        for val in board_free_space:
            ans_dict = self.minFun(val, board_list.copy())
            l.append(ans_dict)
        # maxk=-math.inf
        # boardk = []
        # for d in l:
        #     for x,y in d.items():
        #         if x>maxk:
        #             maxk=x
        #             boardk=y
        # ans = {maxk:boardk}
        ans = self.findMax(l)
        return ans
            
    
    def minFun(self, pos, board_list):
        board_list[pos] = self.opp_letter
        board_free_space = self.available_space_player(board_list)
        print("Min",board_list,board_free_space)
        if self.is_winner(self.letter, board_list):
            utility = self.utilityFun(board_free_space, self.WIN)
            # print("W:",utility)
            return utility
        if self.is_opponent_winner(board_list):
            utility = self.utilityFun(board_free_space, self.LOSE)
            # print("L:",utility)
            return {utility:board_list}
        if self.drawEval(board_free_space, board_list):
            return {0:board_list}        
        l = []        
        for val in board_free_space:
            ans_dict = self.maxFun(val, board_list.copy())
            l.append(ans_dict)
        # mink=math.inf
        # boardk = []
        # for d in l:
        #     for x,y in d.items():
        #         if x<mink:
        #             mink=x
        #             boardk=y
        # ans = {mink:boardk}
        ans = self.findMin(l)
        return ans
                
