"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

p_infi = math.inf
n_infi = -math.inf
def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count, o_count = 0,0
    for row in board:
        for box in row:
            if box == X:
                x_count +=1
            elif box == O:
                o_count +=1

    
    if x_count > o_count:
        return O
    else:
        return X        

    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    empty = set()
    for  i, row in enumerate(board):
        for j, box in enumerate(row):
            if box == EMPTY:
                empty.add((i, j))
    return empty
    # raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    if board[action[0]][action[1]] != EMPTY:
        raise NameError("Invalid Action")
        
    
    my_board = copy.deepcopy(board)

    my_board[action[0]][action[1]] = player(my_board)

    return my_board

    # raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        x_boxes = [box for box in row if box == X]
        if len(x_boxes) == 3:
            return X
        o_boxes = [box for box in row if box == O]
        if len(o_boxes) == 3:
            return O
    
    for i in range(len(board)):
        o_count = 0
        x_count = 0
        for row in board:
            if row[i] == X:
                x_count +=1
            if row[i] == O:
                o_count += 1
        if x_count == 3:
            return X
        if o_count == 3:
            return O
    x_count = 0
    o_count = 0
    for i in range(len(board)):
        
        if board[i][i] == X:
           x_count +=1 
        if board[i][i] == O:
           o_count +=1 
        if x_count == 3:
            return X
        if o_count == 3:
            return O
    x_count = 0
    o_count = 0
    for i in range(len(board)):
        
        if board[i][-i-1] == X:
           x_count +=1 
        if board[i][-i-1] == O:
           o_count +=1 
        if x_count == 3:
            return X
        if o_count == 3:
            return O

    return None
    




def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if EMPTY not in [box for row in board for box in row]:
        return True
    elif winner(board) is not None:
        return True
    else:
        return False
    # raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else: 
        return 0
    # raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    my_board = copy.deepcopy(board)

    utilities = []
    my_actions = list(actions(my_board))

    if player(my_board) == X: 
        for action in my_actions:
            present_utility =  minim(result(my_board, action))       
            utilities.append(present_utility)
            if present_utility == 1:
                return action
            
        return my_actions[utilities.index(max(utilities))]
    
    if player(my_board) == O: 
        for action in my_actions:        
            present_utility =  maxim(result(my_board, action))       
            utilities.append(present_utility)
            if present_utility == -1:
                return action
        return my_actions[utilities.index(min(utilities))]
    
           

def maxim(board):

    if terminal(board):

        return utility(board)
    else:
        my_board = copy.deepcopy(board)
        utilities = [] 
        for action in actions(my_board):        
            present_utility =  minim(result(my_board, action))       
            utilities.append(present_utility)
            if present_utility == 1:
                return present_utility
        return max(utilities)
        

def minim(board):

    if terminal(board):

        return utility(board)
    else:
        my_board = copy.deepcopy(board)       
        utilities = [] 
        for action in actions(my_board):        
            present_utility =  maxim(result(my_board, action))       
            utilities.append(present_utility)

            if present_utility == -1:
                return present_utility
        return min(utilities)

    

