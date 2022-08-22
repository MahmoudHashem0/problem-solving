"""
Tic Tac Toe Player
"""

import math
import copy
import random

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
    cells = []
    i=0
    while i<3:
        j=0
        while j<3:
            cell = board[i][j]
            if cell != EMPTY:
                cells.append((i,j))
            j+=1
        i+=1

    players = [X, O]
    Player = players[len(cells)%2!=0]
    return Player


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    cells = []
    i=0
    while i<3:
        j=0
        while j<3:
            cell = board[i][j]
            if cell == EMPTY:
                cells.append((i,j))
            j+=1
        i+=1
    random.shuffle(cells)
    return cells


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    cells = []
    i=0
    while i<3:
        j=0
        while j<3:
            cell = board[i][j]
            if cell != EMPTY:
                cells.append((i,j))
            j+=1
        i+=1
    if action in cells:
        raise Exception

    newboard = copy.deepcopy(board)

    newboard[action[0]][action[1]] = player(board)
    return newboard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winner = EMPTY

    for i in range(3):
        if(EMPTY != board[i][0]==board[i][1]==board[i][2]):
            winner = board[i][0]
            return winner


    for j in range(3):
        if(EMPTY != board[0][j]==board[1][j]==board[2][j]):
            winner = board[0][j]
            return winner
    

    if(EMPTY != board[0][0]==board[1][1]==board[2][2]):
        winner=board[1][1]
        return winner

    if(EMPTY != board[0][2]==board[1][1]==board[2][0]):
        winner=board[1][1]
        return winner
    
    return winner
    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if(winner(board) != EMPTY):
        return True
    
    over = True

    i=0
    while i<3:
        j=0
        while j<3:
            cell = board[i][j]
            if cell == EMPTY:
                over = False
                break
            j+=1
        i+=1

    return over



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    dic = {X:1, O:-1, EMPTY:0}

    return dic[winner(board)]




def myminimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    Player = player(board)
    Actions = actions(board)
    MAX = {'weight':-1, 'action': Actions[0]}
    MIN = {'weight': 1, 'action': Actions[0]}  

    cells = []
    i=0
    while i<3:
        j=0
        while j<3:
            cell = board[i][j]
            if cell != EMPTY:
                cells.append((i,j))
            j+=1
        i+=1


    for action in Actions:
        Result = result(board, action)
        if (not terminal(Result)):
            if Player == X:
                if MAX['weight'] == 1:
                    break
                Myminimax = myminimax(Result)
                if(Myminimax['weight'] > MAX['weight']):
                    MAX['weight'] = Myminimax['weight']
                    MAX['action'] = action
            else:
                if MIN['weight'] == -1:
                    break
                Myminimax = myminimax(Result)
                if(Myminimax['weight'] < MIN['weight']):
                    MIN['weight'] = Myminimax['weight']
                    MIN['action'] = action
        else:
            Utility = utility(Result)
            if Player == X:
                if(Utility > MAX['weight']):
                    MAX['weight'] = Utility
                    MAX['action'] = action
            else:
                if(Utility < MIN['weight']):
                    MIN['weight'] = Utility
                    MIN['action'] = action

    if Player == X:
        return MAX
    else:
        return MIN

def minimax(board):
    if terminal(board):
        return None

    Actions = actions(board)
    if len(Actions) == 9:
        return random.sample(Actions, 1)[0]

    action = myminimax(board)['action']
    return action




