def validate_move(move, board):
    return 1 <= move <= 9 and board.is_available(move)

def get_available_moves(board):
    return (i+1 for i, v in enumerate(board.cells) if v == " ")
