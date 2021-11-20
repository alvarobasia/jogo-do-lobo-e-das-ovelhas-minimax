from typing import List, Tuple


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

        if not block_positions[0] and board[self.position[0] + 1][self.position[1] - 1] == 0:
            print('valid 1')
            valid_moves.append(
                [self.position[0] + 1,  self.position[1] - 1])
        if not block_positions[1] and board[self.position[0] + 1][self.position[1] + 1] == 0:
            print('valid 2')
            valid_moves.append(
                [self.position[0] + 1,  self.position[1] + 1])

        return valid_moves
