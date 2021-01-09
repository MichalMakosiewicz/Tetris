import random
from models.pieces import PIECES


class Piece:

    def __init__(self, board):
        """
        On initialization defina piece position and type.
        """
        self.type = PIECES[random.randrange(len(PIECES))]
        self.position = [0, random.randrange(1, board.size-len(self.type))]

    def reset_piece(self, board):
        """
        Reset piece to start position with random type.
        """
        self.type = PIECES[random.randrange(len(PIECES))]
        self.position = [0, random.randrange(1, board.size-len(self.type))]
