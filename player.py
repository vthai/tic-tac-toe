'''
    Implementation of different tic tac toe AI agent

    @created: 26/11/2016
    @author: veng.thai@gmail.com
'''
import math

'''
    Abstract player class
'''
class Player(object):
    def play(self, move):
        pass

'''
    This is the normal human player
'''
class HumanPlayer(Player):
    def __init__(self, gameboard):
        self.gameboard = gameboard

    def play(self, move):
        self.gameboard.record(move)
        while True:
            # move is a tuple to specify the row and column in the game board
            row, column = tuple(map(int, raw_input().split(' ')))
            if (row, column) not in self.gameboard.legal_moves():
                print ("Error: illegal move, please re-enter the coordinates:"),
                continue
            break
        self.gameboard.record((row, column))
        return (row, column)

'''
    This is the AI agent using Minmax algorithm
'''
class Minmax_player(Player):
    def __init__(self, gameboard, eval_function):
        self.gameboard = gameboard

    def play(self, move):
        pass

    # def max(self, move):
    #     if self.gameboard.game_ends():
    #         return self.eval_function(self.gameboard)

    #     best_value = -math.inf
    #     for move in self.gameboard.legal_moves():
    #         self.gameboard.do_move(move)
    #         value = self.min(maxply - 1)
    #         if best_value is None or value > best_value:
    #             best_value = value
    #         self.gameboard.undo_move()
    #     #print ("Max choose ", best_val)
    #     return best_value
