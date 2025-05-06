import random

class Player:
    def __init__(self, name, marker):
        self.name = name
        self.marker = marker

    def get_move(self, board):
        while True:
            try:
                move = int(input(f"{self.name}'s Turn ({self.marker}): Enter a position (1-9): "))
                return move
            except ValueError:
                print("Invalid input. Enter a number between 1 and 9.")
