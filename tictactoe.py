"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None
winvalue = 2
maxormin = True
v = 0

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
                moves.append([i, j])
    return moves

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # specification says don't change OG board
    turn = player(board)
    newboard = [row[:] for row in board]
    if newboard[action[0]][action[1]] == EMPTY:
        newboard[action[0]][action[1]] = turn
    else:
        raise inputerror
    return newboard

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    for player in [X, O]:
        # Check rows and columns
        for i in range(3):
            if all(cell == player for cell in board[i]) or all(board[j][i] == player for j in range(3)):
                return 1 if player == X else -1
        # Check diagonals
        if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
            return 1 if player == X else -1
    return 0
        

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if utility(board) != 0:
        if utility(board) == 1:
            return X
        else:
            return O
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    taken = 0
    if utility(board) != 0:
        return True
    for i in range(3):
        try:
        # if there's an available spot in this row
            if board[i].index(EMPTY) > -1:
                break
        # if there isnt
        except ValueError:
            taken += 1
            continue
    if taken == 3:
        return True
    else:
        return False

def maxi(board):
    if terminal(board) == True:
        return utility(board)
    v = -2
    # for each action possible
    for i in range(len(actions(board))):
        v = max(v, mini(result(board, actions(board)[i])))
    return v
    
def mini(board):
    if terminal(board) == True:
        return utility(board)
    v = 2
    # for each action possible
    for j in range(len(actions(board))):
        v = min(v, maxi(result(board, actions(board)[j])))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    bestaction = (0, 0)
    if player(board) == X:
        bestvalue = float('inf')     
    else:
        bestvalue = float('-inf')
    turn = player(board)
    if terminal(board) == True:
        return None
    # X wants to maximize win value
    if turn == X:
        bestvalue = maxi(board)
        # for each action possible on this board
        for i in range(len(actions(board))):
            # if the best max value equals the best min value for this action
            if bestvalue == mini(result(board, actions(board)[i])):
                bestaction = actions(board)[i]
                break
    # O wants to minimize win value
    else:
        bestvalue = mini(board)
        print(f"{bestvalue}")
        # for each action possible on this board
        for j in range(len(actions(board))):
            # if the best original min value equals the best max value for this action
            if bestvalue == maxi(result(board, actions(board)[j])):
                bestaction = actions(board)[j]
                break

    return bestaction
