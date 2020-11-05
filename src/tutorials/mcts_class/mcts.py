#
# MCTS algorithm implementation
#

# packages
import math
import random

# tree node class definition
class TreeNode():
    # class constructor (create tree node class instance)
    def __init__(self, board, parent):
        # init associated board state
        self.board = board
        
        # init is node terminal flag
        if self.board.is_win() or self.board.is_draw():
            # we have a terminal node
            self.is_terminal = True
        
        # otherwise
        else:
            # we have a non-terminal node
            self.is_terminal = False
        
        # init is fully expanded flag
        self.is_fully_expanded = self.is_terminal
        
        # init parent node if available
        self.parent = parent
        
        # init the number of node visits
        self.visits = 0
        
        # init the total score of the node
        self.score = 0
        
        # init current node's children
        self.children = {}

# MCTS class definition
class MCTS():
    # search for the best move in the current position
    def search(self, initial_state):
        # create root node
        self.root = TreeNode(initial_state, None)

        # walk through 1000 iterations
        for iteration in range(1000):
            # select a node (selection phase)
            node = self.select(self.root)
            
            # scrore current node (simulation phase)
            score = self.rollout(node.board)
            
            # backpropagate results
            self.backpropagate(node, score)
        
        # pick up the best move in the current position
        try:
            return get_best_move(self.root, 0)
        
        except:
            pass
    
    # select most promising node
    def select(self, node):
        pass
    
    # simulate the game via making random moves until reach end of the game
    def rollout(self, board):
        pass
    
    # backpropagate the number of visits and score up to the root node
    def backpropagate(self, node, score):
        pass
    
    # select the best node basing on UCB1 formula
    def get_best_move(self, node, exploration_constant):
        pass













