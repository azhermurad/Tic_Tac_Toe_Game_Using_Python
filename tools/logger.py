from pathlib import Path
from datetime import datetime

class Logger:
    def __init__(self, game_number, p1_name, p2_name):
        self.log_dir = Path("tic_tac_toe/game_log") / f"game{game_number}"
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.log_file = self.log_dir / "log.txt"
        self.move_number = 0
        self._init_log(p1_name, p2_name)

    def _init_log(self, p1, p2):
        with self.log_file.open("w") as f:
            f.write(f"Game Log - {datetime.now()}\n")
            f.write(f"Players:\n- {p1} (X)\n- {p2} (O)\n\n")

    def log_players(self, p1, p2):
        with self.log_file.open("a") as f:
            f.write(f"First move: {p1.name}\n\nMoves:\n")

    def log_move(self, player, pos, board):
        self.move_number += 1
        with self.log_file.open("a") as f:
            f.write(f"Move {self.move_number}: {player.name} -> Position {pos}\n")
            f.write(f"Board After Move {self.move_number}:\n{board.display()}\n\n")

    def log_result(self, result):
        with self.log_file.open("a") as f:
            f.write(f"Result: {result}\n")
