"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None
winvalue = 2

class inputerror(Exception):
    # raises exception if occupied square clicked
    print("Invalid cell.")
    pass

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
    moves = []
    # row itterator
    for i in range(3):
        # column itterator
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.append(f"({i}, {j})")
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # specification says don't change OG board
    turn = player(board)
    newboard = board
    if newboard[action[0]][action[1]] == EMPTY:
        newboard[action[0]][action[1]] = turn
    else:
        raise inputerror
    return newboard

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
    return 0
        

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if winvalue == 1:
        return X
    if winvalue == -1:
        return O
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winvalue != 2:
        return True
    if actions(board) == []:
        return True
    return False

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
