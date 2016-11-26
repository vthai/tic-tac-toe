'''
    Implementation of different tic tac toe AI agent

    @created: 26/11/2016
    @author: veng.thai@gmail.com
'''

import numpy as np

import player

'''
    This is the gameboard for the tic tac toe, it record the status of the game move and provides
    method to determine who wins a game and what are legal moves in a game
'''
class TicTacToeBoard(object):
    def __init__(self, n):
        self.n = n
        self.board = np.zeros((3, 3), dtype=int)
        self.symbol = {0: '.', 1: 'x', -1: 'o'}
        self.name = {1: 'White (x)', -1: 'Black (o)'}
        self.turn = 1;

    def display(self):
        print ''
        for row in range(0, self.n):
            rowStr = [self.symbol[cell] for cell in self.board[row, :]]
            print '\t' + ' '.join(rowStr)
        print ''

    def current_player_name(self):
        return self.name[self.turn]

    def previous_player_name(self):
        return self.name[self.turn * -1]

    def clone(self):
        t3 = TicTacToeBoard(self.n)
        return t3

    def record(self, move):
        if move is not None:
            self.board[move] = self.turn
            self.turn = self.turn * -1

    def legal_moves(self):
        x, y = np.where(self.board == 0)
        return zip(x, y)

    def game_ends(self, last_move):
        if last_move is None:
            return False

        row = last_move[0]
        column = last_move[1]

        left = max(0, column - 3)
        right = min(self.n, column + 3)
        top = max(0, row - 3)
        bottom = min(self.n, row + 3)

        left_to_right = self.board[row, left:right]
        total_3_cell = left_to_right == 1
        if total_3_cell.sum() == 3:
            return True
        
        total_3_cell = left_to_right == -1
        if total_3_cell.sum() == 3:
            return True

        top_to_bottom = self.board[top:bottom, column]
        total_3_cell = top_to_bottom == 1
        if total_3_cell.sum() == 3:
            return True
        
        total_3_cell = top_to_bottom == -1
        if total_3_cell.sum() == 3:
            return True

        diag_row = range(top, bottom)
        diag_column = range(left, right)

        diag_left = self.board[diag_row, diag_column]
        total_3_cell = diag_left == 1
        if total_3_cell.sum() == 3:
            return True
        
        total_3_cell = diag_left == -1
        if total_3_cell.sum() == 3:
            return True

        diag_column.reverse()
        diag_right = self.board[diag_row, diag_column]
        total_3_cell = diag_right == 1
        if total_3_cell.sum() == 3:
            return True
        
        total_3_cell = diag_right == -1
        if total_3_cell.sum() == 3:
            return True

        return False


class Game(object):

    def __init__(self, n=3):
        self.t3_board = TicTacToeBoard(n)
        self.player1 = player.HumanPlayer(self.t3_board.clone())
        self.player2 = player.HumanPlayer(self.t3_board.clone())
        self.players = {1: self.player1, -1: self.player2}

    def start(self):
        last_move = None

        while not self.t3_board.game_ends(last_move):
            self.t3_board.display()

            print 'Legal moves coordinates:', self.t3_board.legal_moves()
            print '\nInput a coordinate to move to by specifying the row and column indexes (seperated by a space)'
            print 'Player %s to move:' %(self.t3_board.current_player_name()),
            
            move = self.players[self.t3_board.turn].play(last_move)
            self.t3_board.record(move)
            last_move = move

        print '\nGame ends with player %s wins' %(self.t3_board.previous_player_name())
        self.t3_board.display()


if __name__ == '__main__':
    print 'Tic Tac Toe game'

    game = Game()
    game.start()