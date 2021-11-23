from typing import List, Tuple
from domain.Player import Player


def minimax(board: List[List[int]], deep, player: Player):
    if player == Player.SHEEP:
        best = [-1, -1, -float("inf")]
    else:
        best = [-1, -1, float("inf")]

    # valor-minimax(estado) = avaliacao(estado)
    if deep == 0 or end_game(board):
        value = evaluation(board)
        return [best[0], best[1], value]

    if player == Player.SHEEP:
        for cell in allowed_cells_sheep(board):
            position_row = cell[0]
            position_column = cell[1]
            board[position_row][position_column] = 'S'
            value = minimax(board, deep - 1, Player.WOLF)
            board[position_row][position_column] = 0
            value[0], value[1] = position_row, position_column

            if player == Player.SHEEP:
                if value[2] > best[2]:
                    best = value
            else:
                if value[2] < best[2]:
                    best = value

    if player == Player.WOLF:
        for cell in allowed_cells_wolf(board):
            position_row = cell[0]
            position_column = cell[1]
            board[position_row][position_column] = 'W'
            value = minimax(board, deep - 1, Player.SHEEP)
            board[position_row][position_column] = 0
            value[0], value[1] = position_row, position_column

            if player == Player.WOLF:
                if value[2] > best[2]:
                    best = value
            else:
                if value[2] < best[2]:
                    best = value

    return best


def end_game(board: List[List[int]]):
    return winner_wolf(board) or winner_sheep(board)


def winner_wolf(board: List[List[int]]):
    first_line = board[0]
    for value in first_line:
        if value == 'W':
            return True

    return False


def winner_sheep(board: List[List[int]]):
    wolf_position = None
    for x, row in enumerate(board):
        for y, value in enumerate(row):
            if value == 'W':
                wolf_position = [x, y]

    possible_moves = [[wolf_position[0] - 1, wolf_position[1] - 1], [wolf_position[0] - 1, wolf_position[1] + 1],
                      [wolf_position[0] + 1, wolf_position[1] - 1], [wolf_position[0] + 1, wolf_position[1] + 1]]
    sheep_victory = True
    for move in possible_moves:
        if move[0] < 0 or move[0] > 7 or move[1] < 0 or move[1] > 7:
            continue

        if board[move[0]][move[1]] == 'S':
            continue

        sheep_victory = False

    return sheep_victory


def evaluation(board: List[List[int]]):
    if winner_wolf(board):
        return -1
    if winner_sheep(board):
        return 1
    return 0


def allowed_cells_sheep(board: List[List[int]]):
    cells = []
    for x, row in enumerate(board):
        for y, value in enumerate(row):
            if value == 'S':
                block_positions = [False, False]
                last_line = False
                if y == 0:
                    block_positions[0] = True
                if y == 7:
                    block_positions[1] = True

                if x >= 7:
                    last_line = True

                if not block_positions[0] and not last_line and board[x + 1][y - 1] == 0:
                    cells.append([x + 1,  y - 1])

                if not block_positions[1] and not last_line and board[x + 1][y + 1] == 0:
                    cells.append([x + 1,  y + 1])

    return cells


def allowed_cells_wolf(board: List[List[int]]):
    cells = []
    for x, row in enumerate(board):
        for y, value in enumerate(row):
            if value == 'W':
                if x + 1 < 7 and y - 1 > 0 and board[x + 1][y - 1] == 0:
                    cells.append([x + 1, y - 1])
                if x + 1 < 7 and y + 1 < 7 and board[x + 1][y + 1] == 0:
                    cells.append([x + 1, y + 1])
                if x - 1 < 0 and y - 1 > 0 and board[x - 1][y - 1] == 0:
                    cells.append([x - 1, y - 1])
                if x - 1 < 0 and y + 1 < 7 and board[x - 1][y + 1] == 0:
                    cells.append([x - 1, y + 1])

    return cells
