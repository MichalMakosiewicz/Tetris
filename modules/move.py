from copy import deepcopy


def get_left_move(piece_position):
    """
    Returns piece new position after left move.

    Return: list
    """
    new_piece_position = [piece_position[0], piece_position[1] - 1]
    return new_piece_position


def get_right_move(piece_position):
    """
    Returns piece new position after right move.
    
    Return: list
    """
    new_piece_position = [piece_position[0], piece_position[1] + 1]
    return new_piece_position


def get_down_move(piece_position):
    """
    Returns piece new position after down move.

    Return: list
    """
    new_piece_position = [piece_position[0] + 1, piece_position[1]]
    return new_piece_position


def rotate_clockwise(piece_type):
    """
    Returns piece new type after clockwise rotation.

    Return: list
    """
    piece_copy = deepcopy(piece_type)
    reverse_piece = piece_copy[::-1]
    return [list(elem) for elem in zip(*reverse_piece)]


def rotate_anticlockwise(piece_type):
    """
    Returns piece new type after anticlockwise rotation.

    Return: list
    """
    piece_copy = deepcopy(piece_type)
    piece_1 = rotate_clockwise(piece_copy)
    piece_2 = rotate_clockwise(piece_1)
    return rotate_clockwise(piece_2)


def check_collisions(board, current_piece, piece_position):
    """
    Check if piece colide after move.

    Return: boolean
    """
    current_piece_size_x = len(current_piece)
    current_piece_size_y = len(current_piece[0])
    for i in range(current_piece_size_x):
        for j in range(current_piece_size_y):
            if board[piece_position[0]+i][piece_position[1]+j] == 1 and current_piece[i][j] == 1:
                return False
    return True


def can_move_left(board, piece):
    """
    Check if piece can move left.
    """
    piece_pos = get_left_move(piece.position)
    return check_collisions(board.board, piece.type, piece_pos)


def can_move_right(board, piece):
    """
    Check if piece can move right.

    Return: boolean
    """
    piece_pos = get_right_move(piece.position)
    return check_collisions(board.board, piece.type, piece_pos)


def can_move_down(board, piece):
    """
    Check if piece can move down.

    Return: boolean
    """
    piece_pos = get_down_move(piece.position)
    return check_collisions(board.board, piece.type, piece_pos)


def can_rotate_anticlockwise(board, piece):
    """
    Check if piece can rotate anticlockwise.

    Return: boolean
    """
    curr_piece = rotate_anticlockwise(piece.type)
    return check_collisions(board.board, curr_piece, piece.position)


def can_rotate_clockwise(board, piece):
    """
    Check if piece can rotate clockwise.

    Return: boolean
    """
    curr_piece = rotate_clockwise(piece.type)
    return check_collisions(board.board, curr_piece, piece.position)


def make_move(player_input, board, piece):
    """
    Updates piece position and type. Place old pice on board

    Return: string
    """
    ERR_MSG = ""
    if player_input not in ['a', 's', 'd', 'w']:
        ERR_MSG = "Wrong input!"
    elif player_input == 'a' and can_move_left(board, piece):
        piece.position = get_left_move(piece.position)
    elif player_input == 'd' and can_move_right(board, piece):
        piece.position = get_right_move(piece.position)
    elif player_input == 'w' and can_rotate_anticlockwise(board, piece):
        piece.type =rotate_anticlockwise(piece.type)
    elif player_input == 's' and can_rotate_clockwise(board, piece):
        piece.type = rotate_clockwise(piece.type)
    else:
        ERR_MSG = "That is not a valid move!"

    if ERR_MSG == "":
        piece.position = get_down_move(piece.position)

    if not can_move_down(board, piece):
        board.merge_piece(piece)
        piece.reset_piece(board)

    return ERR_MSG
