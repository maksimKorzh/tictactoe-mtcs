#
# AI that learns to play tictactoe using
#        reinforcement learning
#             (MCTS + NN)
#

# packages
from copy import deepcopy

# tictactoe board class
class Board():
    # init tictactoe instance
    def __init__(self, opponent=None):
        # define game parameters
        self.player_1 = 'x'
        self.player_2 = 'o'
        self.empty_square = '.'
        
        # define game board
        self.position = {}
        
        # reset board
        self.reset_board()
        
        # if opponent to play
        if opponent is not None:            
            # copy opponents board state
            self.__dict__ = deepcopy(opponent.__dict__)

    # reset board
    def reset_board(self):
        # loop over board rows
        for row in range(3):
            # loop over board columns
            for col in range(3):
                # set empty square at board coordinates [row, col]
                self.position[row, col] = self.empty_square

    # make move
    def make_move(self, col, row):
        # create opponents tictactoe instance
        board = Board(self)
        
        # make move
        board.position[row, col] = self.player_1
        
        # switch side to move
        (board.player_1, board.player_2) = (board.player_2, board.player_1)
        
        # return opponent's board state
        return board
    
    # draw detection
    def is_draw(self):
        # loop over board squares
        for row, col in self.position:
            # if empty square still available on board
            if self.position[row, col] == self.empty_square:
                # game is going on
                return False
        
        # otherwise game is drawn
        return True
    
    # win detection
    def is_win(self):
        #
        # horizontal sequence detection
        #
        
        # loop over board rows
        for row in range(3):
            # winning sequence list
            winning = []
            
            # loop over board columns
            for col in range(3):
                # found player 2 move
                if self.position[row, col] == self.player_2:
                    # append move to winning sequence
                    winning.append((row, col))
                
                # if three in the row
                if len(winning) == 3:
                    return True
        
        #
        # vertical sequence detection
        #
        
        # loop over board rows
        for col in range(3):
            # winning sequence list
            winning = []
            
            # loop over board columns
            for row in range(3):
                # found player 2 move
                if self.position[row, col] == self.player_2:
                    # append move to winning sequence
                    winning.append((row, col))
                
                # if three in the row
                if len(winning) == 3:
                    return True
        
        #
        # 1st diagonal sequence detection
        #
        
        # winning sequence list
        winning = []
        
        # loop over board rows
        for row in range(3):
            # set col equal to row
            col = row
                
            # found player 2 move
            if self.position[row, col] == self.player_2:
                # append move to winning sequence
                winning.append((row, col))
            
        # if three in the row
        if len(winning) == 3:
            return True
        
        #
        # 2nd diagonal sequence detection
        #
        
        # winning sequence list
        winning = []
        
        # loop over board rows
        for row in range(3):
            # set col equal to row
            col = 3 - row - 1
                
            # found player 2 move
            if self.position[row, col] == self.player_2:
                # append move to winning sequence
                winning.append((row, col))
            
        # if three in the row
        if len(winning) == 3:
            return True
        
        # by defualt
        return False
            
    
    # play versus human loop
    def play_human_loop(self):
        # print game greetings
        print('\n\n    Tic Tac Toe (Human vs Human mode) by Code Monkey King\n')
        print('print move in format [column][row]: "0,0" or "exit" to quit\n')
        
        # print board
        print(self)
        
        # get user input
        user_input = ''
        
        # game loop
        while True:            
            # get user input
            user_input = input('> ')
            
            # escape condition
            if user_input == 'exit': break
            
            # empty input
            if user_input == '': continue
            
            # parse user input
            try:
                # extract move coordinates
                coordinates = user_input.split(',')
                col = int(coordinates[0]) - 1
                row = int(coordinates[1]) - 1
                
                # move legality checking
                if self.position[row, col] != self.empty_square:
                    print('Illegal move!')
                    continue
                
                # make move
                self = self.make_move(col, row)
                
                # print board
                print(self)
                
                # on win
                if self.is_win():
                    print('Player "%s" won!' % self.player_2)
                    self.reset_board()
                    print(self)
                
                # on draw
                elif self.is_draw():
                    print('Game is drawn!')
                    self.reset_board()
                    print(self)

            except:
                print('Illegal command!')

    # print board
    def __str__(self):
        # define board string
        board_string = ''
    
        # loop over board rows
        for row in range(3):
            # loop over board columns
            for col in range(3):
                # append each square's value to board string
                board_string += ' %s' % self.position[row, col]
            
            board_string += '\n'
        
        # if player 'x' to play
        if self.player_1 == 'x':
            # prepend player
            board_string = '\n--------------\n "x" to play:\n--------------\n' + board_string
        
        # if player 'o' to play
        elif self.player_1 == 'o':
            # prepend player
            board_string = '\n--------------\n "o" to play:\n--------------\n' + board_string
        
        # return board representation as string
        return board_string

if __name__ == '__main__':
    # init board instance
    board = Board()
            
    # run Human vs Human game
    board.play_human_loop()
















            
        
