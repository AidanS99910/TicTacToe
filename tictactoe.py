"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    board = [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
    return board


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xcount = 0
    ocount = 0
    # rows
    for i in range(3):
        # columns
        for j in range(3):
            if board[i][j] == X:
                xcount += 1
            elif board[i][j] == O:
                ocount += 1
    if xcount == ocount:
        return X
    if xcount > ocount:
        return O
    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    xoro = X
    winvalue = 1
    for n in range(2):
        if board == [[xoro, EMPTY, EMPTY],
                    [EMPTY, xoro, EMPTY],
                    [EMPTY, EMPTY, xoro]]:
            return winvalue
        if board == [[xoro, xoro, xoro],
                    [EMPTY, EMPTY, EMPTY],
                    [EMPTY, EMPTY, EMPTY]]:
            return winvalue
        if board == [[xoro, EMPTY, EMPTY],
                    [xoro, EMPTY, EMPTY],
                    [xoro, EMPTY, EMPTY]]:
            return winvalue
        if board == [[EMPTY, xoro, EMPTY],
                    [EMPTY, xoro, EMPTY],
                    [EMPTY, xoro, EMPTY]]:
            return winvalue
        if board == [[EMPTY, EMPTY, xoro],
                    [EMPTY, xoro, EMPTY],
                    [xoro, EMPTY, EMPTY]]:
            return winvalue
        if board == [[EMPTY, EMPTY, xoro],
                    [EMPTY, EMPTY, xoro],
                    [EMPTY, EMPTY, xoro]]:
            return winvalue
        if board == [[EMPTY, EMPTY, EMPTY],
                    [xoro, xoro, xoro],
                    [EMPTY, EMPTY, EMPTY]]:
            return winvalue
        if board == [[EMPTY, EMPTY, EMPTY],
                    [EMPTY, EMPTY, EMPTY],
                    [xoro, xoro, xoro]]:
            return winvalue
        xoro = O
        winvalue = -1
        

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
            
    
    raise NotImplementedError

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
