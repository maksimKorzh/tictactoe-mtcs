#
# AI that learns to play Tic Tac Toe using
#        reinforcement learning
#                (MCTS)
#

# packages
from copy import deepcopy

# Tic Tac Toe board class
class Board():
    # create constructor (init board class instance)
    def __init__(self, board=None):
        # define players
        self.player_1 = 'x'
        self.player_2 = 'o'
        self.empty_square = '.'
        
        # define board position
        self.position = {}
        
        # init (reset) board
        self.init_board()
        
        # create a copy of a previous board state if available
        if board is not None:
            self.__dict__ = deepcopy(board.__dict__)
    
    # init (reset) board
    def init_board(self):
        # loop over board rows
        for row in range(3):
            # loop over board columns
            for col in range(3):
                # set every board square to empty square
                self.position[row, col] = self.empty_square
    
    # make move
    def make_move(self, row, col):
        # create new board instance
        board = Board(self)
        
        # make move
        board.position[row, col] = self.player_1
        
        # swap players
        (board.player_1, board.player_2) = (board.player_2, board.player_1)
    
        # return new board state
        return board
    
    # get whether the game is drawn
    def is_draw(self):
        # loop over board squares
        for row, col in self.position:
            # empty square is available
            if self.position[row, col] == self.empty_square:
                # this is not a draw
                return False
        
        # by default we return a draw
        return True
    
    # get whether the game is won
    def is_win(self):
        ##################################
        # vertical sequence detection
        ##################################
        
        # loop over board columns
        for col in range(3):
            # define winning sequence list
            winning_sequence = []
            
            # loop over board rows
            for row in range(3):
                # if found same next element in the row
                if self.position[row, col] == self.player_2:
                    # update winning sequence
                    winning_sequence.append((row, col))
                    
                # if we have 3 elements in the row
                if len(winning_sequence) == 3:
                    # return the game is won state
                    return True
        
        ##################################
        # horizontal sequence detection
        ##################################
        
        # loop over board columns
        for row in range(3):
            # define winning sequence list
            winning_sequence = []
            
            # loop over board rows
            for col in range(3):
                # if found same next element in the row
                if self.position[row, col] == self.player_2:
                    # update winning sequence
                    winning_sequence.append((row, col))
                    
                # if we have 3 elements in the row
                if len(winning_sequence) == 3:
                    # return the game is won state
                    return True
    
        ##################################
        # 1st diagonal sequence detection
        ##################################
        
        # define winning sequence list
        winning_sequence = []
        
        # loop over board rows
        for row in range(3):
            # init column
            col = row
        
            # if found same next element in the row
            if self.position[row, col] == self.player_2:
                # update winning sequence
                winning_sequence.append((row, col))
                
            # if we have 3 elements in the row
            if len(winning_sequence) == 3:
                # return the game is won state
                return True
        
        ##################################
        # 2nd diagonal sequence detection
        ##################################
        
        # define winning sequence list
        winning_sequence = []
        
        # loop over board rows
        for row in range(3):
            # init column
            col = 3 - row - 1
        
            # if found same next element in the row
            if self.position[row, col] == self.player_2:
                # update winning sequence
                winning_sequence.append((row, col))
                
            # if we have 3 elements in the row
            if len(winning_sequence) == 3:
                # return the game is won state
                return True
        
        # by default return non winning state
        return False
        
    # print board state
    def __str__(self):
        # define board string representation
        board_string = ''
        
        # loop over board rows
        for row in range(3):
            # loop over board columns
            for col in range(3):
                board_string += ' %s' % self.position[row, col]
            
            # print new line every row
            board_string += '\n'
        
        # prepend side to move
        if self.player_1 == 'x':
            board_string = '\n--------------\n "x" to move:\n--------------\n\n' + board_string
        
        elif self.player_1 == 'o':
            board_string = '\n--------------\n "o" to move:\n--------------\n\n' + board_string
                        
        # return board string
        return board_string

# main driver
if __name__ == '__main__':
    # create board instance
    board = Board()

    # define custom board state
    board.position = {
        (0, 0): 'o', (0, 1): 'o', (0, 2): 'x',
        (1, 0): 'x', (1, 1): 'x', (1, 2): 'o',
        (2, 0): 'o', (2, 1): 'o', (2, 2): 'x',
    }
    
    # swap players manually
    board.player_2 = 'x'
    board.player_1 = 'o'
    
    # print board
    print(board)
    print('player_2: "%s"' % board.player_2)
    
    # distinguish between won and drawn states
    if board.is_win():
        print('Game is won:', board.is_win())
    else:
        print('Game is drawn:', board.is_draw())

    
    
    
    
    
    
