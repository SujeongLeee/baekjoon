import sys
import numpy as np
import copy
input = sys.stdin.readline

#height, width input
board_height, board_width = map(int, input().split())

#board_status input
board_status = []

for i in range(board_height):
    board_status.append(list(input().rstrip()))

board_status = np.array(board_status)

# def move func
def move_up_left(line, target):
    target_index = np.where(line == target)[0][0]

    if line[target_index - 1] == '.':
        line[target_index - 1] = target
        line[target_index] = '.'
        goal_reached = 0
    elif line[target_index - 1] == '0':
        if target =='R':
            goal_reached = 1
        else:
            goal_reached = -1
    else:
        goal_reached = 0
    return goal_reached

def move_down_right(line, target):
    target_index = np.where(line == target)[0][0]

    if line[target_index + 1] == '.':
        line[target_index + 1] = target
        line[target_index] = '.'
        goal_reached = 0
    elif line[target_index + 1] == '0':
        if target == 'R':
            goal_reached = 1
            print(0, goal_reached)
        else:
            goal_reached = -1
    else:
        goal_reached = 0
    return goal_reached

# up, right, down, left
move = [move_up_left, move_down_right, move_down_right, move_up_left]


# def board func
def board_shift(board, direc):
    while True:
        board_record = copy.deepcopy(board)
        # move once
        goal_reached = 0
        for i in range(board_height):
            if direc in [0, 2]:
                line = board[:, i]
            else:
                line = board[i, :]
            if ('R' in line) and ('B' in line):
                R_index = np.where(line == 'R')[0][0]
                B_index = np.where(line == 'B')[0][0]
                if direc in [0, 3]:
                    if R_index < B_index:
                        goal_reached = move[direc](line, 'R')
                        goal_reached = move[direc](line, 'B')
                    else:
                        goal_reached = move[direc](line, 'B')
                        goal_reached = move[direc](line, 'R')
                else:
                    if R_index < B_index:
                        goal_reached = move[direc](line, 'B')
                        goal_reached = move[direc](line, 'R')
                    else:
                        goal_reached = move[direc](line, 'R')
                        goal_reached = move[direc](line, 'B')
            elif 'R' in line:
                goal_reached = move[direc](line, 'R')
            elif 'B' in line:
                goal_reached = move[direc](line, 'B')
            else:
                continue
        # goal check
        print(1, goal_reached)
        if (goal_reached == 1) or (goal_reached == -1):
            return board, goal_reached
        # if board does not change after the move, break the loop
        if np.array_equal(board_record, board):
            return board, goal_reached

def find_search_direc(board):
    R_index = np.where(board == 'R')
    R_index = [R_index[0][0], R_index[1][0]]
    search_direc = []

    if board[R_index[0], R_index[1] - 1] != '#':
        search_direc.append(0)
    elif board[R_index[0] + 1, R_index[1]] != '#':
        search_direc.append(1)
    elif board[R_index[0], R_index[1] + 1] != '#':
        search_direc.append(2)
    elif board[R_index[0] - 1, R_index[1]] != '#':
        search_direc.append(3)

    return search_direc

# BFS
depth = 0
searched_space = {
    depth: [[board_status, 0]]
}

while depth < 10:
    for i in len(searched_space[depth]):
        current_search = searched_space[depth]