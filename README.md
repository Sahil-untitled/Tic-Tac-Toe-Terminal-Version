# ❌⭕ The Console Tic-Tac-Toe Game

This is a simple two-player console-based Tic-Tac-Toe game written in Python. Players select their positions on the 3×3 board alternatively. The one who aligns three symbols either in a row, column, or diagonal, wins.

## 📜 How It Works

- The game comprises a 3×3 grid with numbers from 1 to 9.
- Player 1 gets an `X`, Player 2 gets an `O`.
- The players input their moves by providing the number of an empty cell.
- After each move, the game checks if there is a winner.
- If one player has won, the game ends; otherwise, if no more spaces are left, it's a tie.

## 🧑‍💻 Running the Game

1. Save the code to a file named `tictactoe.py`.
2. On a terminal interface, simply call the Python interpreter to run this file:

```bash
python tictactoe.py
```

3. Follow the instructions on the screen.

## 🧠 Gameplay Example

```
Player X, enter a number(1-9): 1
 X | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
Player O, enter a number(1-9): 5
 X | 2 | 3
---+---+---
 4 | O | 6
---+---+---
 7 | 8 | 9
...
Player X wins!
``` 

## 🛠️ Requirements

- Python 3.x
- No external libraries needed (uses standard input/output)

## 📁 File Structure

```
tictactoe.py
README.md
```
