# 🎮 Tic-Tac-Toe (Command Line Game)

This is a modular, object-oriented command-line implementation of the classic Tic-Tac-Toe game, created for **CS-878 (Spring 2025)** assignment. The game features clean code architecture, structured logging, and interactive two-player gameplay.

---

## ✅ Features

- 🧑‍🤝‍🧑 Two-player human mode
- 🔁 Turn-based gameplay loop
- ✅ Move input validation
- 📊 Win and draw detection
- 🗂️ Game logs stored per session
- 🧱 Modular and maintainable codebase

---

## 🗂️ Project Structure

tic_tac_toe/
├── main.py # Main controller to run the game
├── game/
│ ├── init.py
│ ├── board.py # Board logic (state, win check, draw check)
│ ├── players.py # Player class and input
│ └── utils.py # Input validation and move generators
├── tools/
│ ├── display.py # UI printing helpers
│ └── logger.py # Logger class for saving game logs
└── game_log/ # Auto-created during gameplay







---

## 🚀 How to Run

1. **Clone this repository**:
   ```bash
   git clone https://github.com/yourusername/tic_tac_toe.git
   cd tic_tac_toe


2. **Run the game:**
    ```python main.py


3. **Sample Log Output:**:
Game Log - 2025-05-06 12:34:56
Players:
    - Alice (X)
    - Bob (O)

First move: Alice

Moves:
Move 1: Alice -> Position 5
Move 2: Bob -> Position 1
Move 3: Alice -> Position 9

Board After Move 3:
    O | 2 | 3
    -----------
    4 | X | 6
    -----------
    7 | 8 | X

Result: Alice wins!

