from typing import List
from domain.Minimax import minimax
from domain.Player import Player

from domain.Sheep import Sheep
from domain.Turn import Turn
from domain.Wolf import Wolf
from utils.print_board import print_board


# tabuleiro na posição inicial:

# movimentos serão feitos pelas coordenadas? linha-coluna


class Game:
    sheeps: List[Sheep]
    wolf: Wolf
    turn: Turn
    winner: int
    board: None

    def __init__(self, board):
        self.sheeps = [Sheep((0, 1)), Sheep(
            (0, 3)), Sheep((0, 5)), Sheep((0, 7))]
        self.wolf = Wolf((7, 4))
        self.turn = Turn.PLAYER
        self.winner = None
        self.board = board
        self.play()

    def play(self):
        while self.winner is None:
            print_board([x.position for x in self.sheeps],
                        self.wolf.position)
            if self.turn == Turn.PLAYER and self.winner is None:
                self.player_turn()
                self.turn = Turn.COMPUTER
                if self.is_player_winner():
                    self.winner = Turn.PLAYER
                    print("Você venceu!")
            if self.turn == Turn.COMPUTER and self.winner is None:
                self.comp_turn()
                self.turn = Turn.PLAYER
                if self.is_sheep_winner():
                    self.winner = Turn.COMPUTER
                    print("O computador venceu!")

    def player_turn(self):
        valid_movement = False
        while not valid_movement:
            value = input(
                "Digite a linha e a coluna para o lobo se movimentar: EXEMPLO: Para linha 3 , coluna 5, digite 3 5: \n")
            value = value.split(" ")
            value = [int(value[0]), int(value[1])]
            valid_movement = self.wolf.valid_movement(
                value[0], value[1], self.board)
            if not valid_movement:
                print("Movimento inválido!")

        self.board = self.wolf.move_piece([value[0], value[1]], self.board)

    def comp_turn(self):
        value = minimax(self.board, 4, Player.SHEEP)
        print(value)
        choose_sheep = self.get_best_sheep_to_movement(value[0], value[1])
        print(f"{choose_sheep}")
        for sheep in self.sheeps:
            if sheep.position[0] == choose_sheep.position[0] and sheep.position[1] == choose_sheep.position[1]:
                self.board = sheep.move_piece([value[0], value[1]], self.board)

    def is_player_winner(self):
        return True if self.wolf.position[0] == 0 else False

    def is_sheep_winner(self):
        valid_movements = [True, True, True, True]
        if self.wolf.position[0] - 1 < 0 or self.wolf.position[1] - 1 < 0 or self.board[self.wolf.position[0] - 1][self.wolf.position[1] - 1] == 'S':
            valid_movements[0] = False
        if self.wolf.position[0] - 1 < 0 or self.wolf.position[1] + 1 > 7 or self.board[self.wolf.position[0] - 1][self.wolf.position[1] + 1] == 'S':
            valid_movements[1] = False

        if self.wolf.position[0] + 1 > 7 or self.wolf.position[1] - 1 < 0 or self.board[self.wolf.position[0] + 1][self.wolf.position[1] - 1] == 'S':
            valid_movements[2] = False

        if self.wolf.position[0] + 1 > 7 or self.wolf.position[1] + 1 > 7 or self.board[self.wolf.position[0] + 1][self.wolf.position[1] + 1] == 'S':
            valid_movements[3] = False

        return valid_movements.count(False) == 4

    def get_best_sheep_to_movement(self, position_row, position_column):
        for sheep in self.sheeps:
            valid_moves = sheep.get_valid_moves(self.board)
            print(valid_moves)
            if [position_row, position_column] in valid_moves:
                return sheep
