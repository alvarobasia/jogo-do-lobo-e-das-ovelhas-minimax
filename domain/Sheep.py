from typing import Tuple


class Sheep:
    position: Tuple[int, int]

    def __init__(self, position: Tuple[int, int]):
        self.position = position

    # Move a ovelha de lugar no tabuleiro

    def move_piece(self, position, board):
        board[self.position[0]][self.position[1]] = 0
        board[position[0]][position[1]] = 'S'
        self.position = position
        return board

    def get_valid_moves(self, board):
        valid_moves = []

        block_positions = [False, False]

        if self.position[1] == 0:
            block_positions[0] = True
        if self.position[1] == 7:
            block_positions[1] = True

        if self.position[0] + 1 > 7:
            pos_x = 7
        else:
            pos_x = self.position[0] + 1

        if self.position[1] + 1 > 7:
            pos_y = 7
        else:
            pos_y = self.position[1] + 1

        if self.position[1] - 1 < 0:
            pos_y_m = 0
        else:
            pos_y_m = self.position[1] - 1

        if not block_positions[0] and board[pos_x][pos_y_m] == 0:
            valid_moves.append(
                [pos_x,  pos_y_m])
        if not block_positions[1] and board[pos_x][pos_y] == 0:
            valid_moves.append(
                [pos_x,  pos_y])

        return valid_moves
