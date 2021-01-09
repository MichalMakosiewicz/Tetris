from modules.board import Board
from modules.piece import Piece
from modules.game import Game
from modules import move


def play_game():
    """
    Starts tetris game in terminal.
    """
    board_instance = Board(20)
    current_piece = Piece(board_instance)
    board_instance.print(current_piece)
    game = Game()

    player_move = input()

    while(game.status):
        msg = move.make_move(player_move, board_instance, current_piece)
        board_instance.print(current_piece, msg)
        game.is_over(board_instance, current_piece)
        player_move = input()

    print("GAME OVER!")

if __name__ == "__main__":
    play_game()
