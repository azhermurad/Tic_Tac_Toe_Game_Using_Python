class Board:
    def __init__(self):
        self.cells = [" "] * 9

    def display(self):
        board_str = ""
        for i in range(3):
            row = [self.cells[j] if self.cells[j] != " " else str(j + 1) for j in range(i * 3, i * 3 + 3)]
            board_str += f" {row[0]} | {row[1]} | {row[2]} \n"
            if i < 2:
                board_str += "---|---|---\n"
        return board_str

    def place_marker(self, pos, marker):
        self.cells[pos - 1] = marker

    def is_available(self, pos):
        return self.cells[pos - 1] == " "

    def check_winner(self, marker):
        win_combos = [
            [0,1,2], [3,4,5], [6,7,8],
            [0,3,6], [1,4,7], [2,5,8],
            [0,4,8], [2,4,6]
        ]
        return any(all(self.cells[i] == marker for i in combo) for combo in win_combos)

    def is_draw(self):
        return all(cell != " " for cell in self.cells)
