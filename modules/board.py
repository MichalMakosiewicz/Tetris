import os
from copy import deepcopy

from modules import move


class Board:
    board = []

    def __init__(self, size):
        """
        On initialization create board based on size.
        """
        self.size = size
        board = [[0 for x in range(size)] for y in range(size)]
        for i in range(size):
            board[i][0] = 1
        for i in range(size):
            board[size-1][i] = 1
        for i in range(size):
            board[i][size-1] = 1
        self.board = board

    def print(self, piece, error_message=''):
        """
        Print Board with piece.

        Return: Nothing
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        print("TETRIS\n\n")

        board_copy = deepcopy(self.board)
        curr_piece_size_x = len(piece.type)
        curr_piece_size_y = len(piece.type[0])
        for i in range(curr_piece_size_x):
            for j in range(curr_piece_size_y):
                board_copy[piece.position[0]+i][piece.position[1] +
                                                j] = piece.type[i][j] | self.board[piece.position[0]+i][piece.position[1]+j]

        for i in range(self.size):
            for j in range(self.size):
                if board_copy[i][j] == 1:
                    print("*", end='')
                else:
                    print(" ", end='')
            print("")

        print(" - a: move piece left")
        print(" - d: move piece right")
        print(" - w: rotate piece counter clockwise")
        print(" - s: rotate piece clockwise\n")

        if error_message:
            print(error_message)
        print("Your move:",)

    def merge_piece(self, piece):
        """
        Place piece on Board. Update board.

        Return: Nothing
        """
        curr_piece_size_x = len(piece.type)
        curr_piece_size_y = len(piece.type[0])
        for i in range(curr_piece_size_x):
            for j in range(curr_piece_size_y):
                self.board[piece.position[0]+i][piece.position[1] +
                                                j] = piece.type[i][j] | self.board[piece.position[0]+i][piece.position[1]+j]

        empty_row = [0]*self.size
        empty_row[0] = 1
        empty_row[self.size-1] = 1

        filled_row = [1]*self.size

        filled_rows = 0
        for row in self.board:
            if row == filled_row:
                filled_rows += 1

        filled_rows -= 1

        for i in range(filled_rows):
            self.board.remove(filled_row)

        for i in range(filled_rows):
            self.board.insert(0, empty_row)
