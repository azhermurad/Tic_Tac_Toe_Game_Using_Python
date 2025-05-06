from game.board import Board
from game.players import Player
from game.utils import validate_move, get_available_moves

from tools.display import welcome_message, print_board, announce_winner, prompt_restart
from tools.logger import Logger

def main():
    name1 = input("Please enter Player 1 name: ")
    name2 = input("Please enter Player 2 name: ")

    welcome_message(name1, name2)

    game_number = 1
    while True:
        board = Board()
        logger = Logger(game_number, name1, name2)
        player1 = Player(name1, "X")
        player2 = Player(name2, "O")

        players = [player1, player2]
        current = 0
        logger.log_players(player1, player2)

        while True:
            print_board(board)
            player = players[current]
            move = player.get_move(board)
            if not validate_move(move, board):
                print("Invalid move. Try again.")
                continue

            board.place_marker(move, player.marker)
            logger.log_move(player, move, board)

            if board.check_winner(player.marker):
                print_board(board)
                announce_winner(player.name)
                logger.log_result(f"{player.name} wins!")
                break
            elif board.is_draw():
                print_board(board)
                print("It's a draw!")
                logger.log_result("Draw")
                break

            current = 1 - current

        if not prompt_restart():
            break
        game_number += 1

if __name__ == "__main__":
    main()
