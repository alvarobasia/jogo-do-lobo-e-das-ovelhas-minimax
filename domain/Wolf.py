from typing import Tuple


class Wolf:
    position: Tuple[int, int]

    def __init__(self, position: Tuple[int, int]):
        self.position = position

    def valid_movement(self, position_row, position_col, board) -> bool:

        if position_row < 0 or position_row > 7:
            return False
        if position_col < 0 or position_col > 7:
            return False

        possible_moves = [[self.position[0] - 1, self.position[1] - 1], [self.position[0] - 1, self.position[1] + 1],
                          [self.position[0] + 1, self.position[1] - 1], [self.position[0] + 1, self.position[1] + 1]]

        if [position_row, position_col] not in possible_moves:
            return False

        if board[position_row][position_col] != 0:
            return False

        return True

    def move_piece(self, position, board):
        board[self.position[0]][self.position[1]] = 0
        board[position[0]][position[1]] = 'W'
        self.position = position
        return board
