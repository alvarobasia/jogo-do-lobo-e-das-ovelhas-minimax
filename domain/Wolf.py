from typing import List, Tuple


class Wolf:
    position: Tuple[int, int]

    def __init__(self, position: Tuple[int, int]):
        self.position = position

    # Validação do movimento
    def valid_movement(self, position_row, position_col, board) -> bool:

        # Validar se a peça esta respeitando os limites do tabuleiro
        if position_row < 0 or position_row > 7:
            return False
        if position_col < 0 or position_col > 7:
            return False

        # Validar se a movimentação da peça está sendo feito na diagonal

        possible_moves = [[self.position[0] - 1, self.position[1] - 1], [self.position[0] - 1, self.position[1] + 1],
                          [self.position[0] + 1, self.position[1] - 1], [self.position[0] + 1, self.position[1] + 1]]

        if [position_row, position_col] not in possible_moves:
            return False

        # Validar se tem algum objeto naquela posição
        if board[position_row][position_col] != 0:
            return False

        return True

    # Move o lobo de lugar no tabuleiro
    def move_piece(self, position, board):
        board[self.position[0]][self.position[1]] = 0
        board[position[0]][position[1]] = 'W'
        self.position = position
        return board
