#
# AI that learns to play Tic Tac Toe using
#        reinforcement learning
#             (MCTS + NN)
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
        # create new board instance that inherits from the current state
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
    
    # generate legal moves to play in the current position
    def generate_states(self):
        # define states list (move list - list of available actions to consider)
        actions = []
        
        # loop over board rows
        for row in range(3):
            # loop over board columns
            for col in range(3):
                # make sure that current square is empty
                if self.position[row, col] == self.empty_square:
                    # append available action/board state to action list
                    actions.append(self.make_move(row, col))
        
        # return the list of available actions (board class instances)
        return actions
        
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
    print('This is initial board state:')
    print(board)

    # generate available actions
    actions = board.generate_states()
    
    # take action (make move on board)
    board = actions[0]
    
    # print updated board state
    print('first generated move has been made on board:')
    print(board)
    
    # generate available actions after first move has been made
    actions = board.generate_states()

    # take action (make move on board)
    board = actions[3]
    print(board)

    # generate available actions after first move has been made
    actions = board.generate_states()
    
    print('\n\n\n\n Generating states...')
    # loop over generated action
    for action in actions:
        # print current action
        print(action)
    
    
    
    
