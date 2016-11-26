'''
    Implementation of different tic tac toe AI agent

    @created: 26/11/2016
    @author: veng.thai@gmail.com
'''

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
    def play(self, move):
        pass
