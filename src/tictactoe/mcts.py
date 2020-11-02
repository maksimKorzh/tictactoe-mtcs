#
# MCTS class implementation
#

# packages
import random
import math

# define tree node class
class TreeNode():
    def __init__(self, board, parent):
        self.board = board
        
        if board.is_win() or board.is_draw():
            self.is_terminal = True
        else:
            self.is_terminal = False

        self.is_fully_expanded = self.is_terminal
        self.parent = parent
        self.visits = 0
        self.total_score = 0
        self.children = {}

# MCTS class definition
class MCTS():
    # exploration constant
    constant = 2#1 / math.sqrt(2)

    # search best move
    def search(self, initial_state):
        # create root node
        self.root = TreeNode(initial_state, None)

        # search iterations
        for iteration in range(1000):
            # select node
            node = self.select_node(self.root)

            # rollout
            score = self.rollout(node.board)        

            # backpropagation
            self.backpropagate(node, score)

        # get best move
        try:
            return self.get_best_move(self.root, 0)
        except:
            return False

    # select node
    def select_node(self, node):
        # if not is not the won position
        while not node.is_terminal:
            
            # figure out whether the node is expanded or not
            if node.is_fully_expanded:
                # get best move for fully expanded node
                node = self.get_best_move(node, self.constant)
            
            # otherwise expand node
            else:
                return self.expand(node)

        # otherwise we have a won position in the node, so just return it
        return node

    # expand node
    def expand(self, node):
        # generate moves
        moves = node.board.generate_moves()
        
        # loop over moves
        for move in moves:    
            # make sure move is not available in child nodes
            if str(move.position) not in node.children:
                # create new node for current move
                new_node = TreeNode(move, node)
                
                # add new node to child nodes '<board>': '<new_node>'
                node.children[str(move.position)] = new_node

                # get fully expanded condition
                if len(moves) == len(node.children):
                    # set fully expanded flag
                    node.is_fully_expanded = True

                # return new node
                return new_node

        print('Should never get here!')
                
    # random rollout
    def rollout(self, board):
        # make random moves until reach the end of games
        while not board.is_win():
            try:
                # make move on board
                board = random.choice(board.generate_moves())

            except:
                # draw
                return 0

        # get score
        if board.is_win() and board.player_2 == 'x': return 1
        elif board.is_win() and board.player_2 == 'o': return -1
        
    # backpropagation
    def backpropagate(self, node, score):
        while node is not None:
            node.visits += 1
            node.total_score += score
            node = node.parent
    
    # get best move (UCB1 formula)
    def get_best_move(self, node, constant):
        # define best and best nodes list
        best_score = float('-inf')
        best_moves = []
        
        # loop over root node's children
        for move in node.children.values():
            # get current player
            if move.board.player_2 == 'o': player = -1
            elif move.board.player_2 == 'x': player = 1

            # get best score via applying UCB1 formula
            move_score = player * move.total_score / move.visits + constant * math.sqrt(2 * math.log(node.visits) / move.visits)
            
            # if score is increased
            if move_score > best_score:
                # update best score and best nodes
                best_score = move_score
                best_moves = [move]
            
            elif move_score == best_score:
                best_moves.append(move)

        return random.choice(best_moves)
            

