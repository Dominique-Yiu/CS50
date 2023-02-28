"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


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
    if board == initial_state():
        return X
    xCounter = 0
    oCounter = 0
    for row in board:
        xCounter += row.count(X)
        oCounter += row.count(O)
    if xCounter == oCounter:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    available_move = list()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                available_move.append((i, j))
    return available_move


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    boardCopy = copy.deepcopy(board)
    try:
        if boardCopy[action[0]][action[1]] != EMPTY:
            raise IndexError
        else:
            boardCopy[action[0]][action[1]] = player(board)
            return boardCopy
    except IndexError:
        print("Spot was already occupied.")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in range(3):
        if (board[row][0] == board[row][1] == board[row][2]) and (board[row][0] != EMPTY):
            return board[row][0]
    for col in range(3):
        if (board[0][col] == board[1][col] == board[2][col]) and (board[0][col] != EMPTY):
            return board[0][col]
    if ((board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0])) and (board[1][1] != EMPTY):
        return board[1][1]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    empltyCounter = 0
    for row in board:
        empltyCounter += row.count(EMPTY)
    if winner(board) != None:
        return True
    elif empltyCounter == 0:
        return True
    else:
        return False


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


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    current_player = player(board)

    if current_player == X:
        v = -math.inf
        for action in actions(board):
            k = minValue(result(board, action))   
            if k > v:
                v = k
                best_move = action
    else:
        v = math.inf
        for action in actions(board):
            k = maxValue(result(board, action)) 
            if k < v:
                v = k
                best_move = action
    return best_move

def maxValue(board):
    val = -math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        val = max(val, minValue(result(board, action)))
    return val

def minValue(board):
    val = math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        val = min(val, maxValue(result(board, action)))
    return val