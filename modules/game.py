from modules import move

class Game:

    def __init__(self):
        """
        On initialization set status of game.
        """
        self.status = True

    def is_over(self, board, piece):
        """
        Update game status if game over.

        Return: Nothing
        """
        if not move.can_move_down(board, piece) and piece.position[0] == 0:
            self.status = False
