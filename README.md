🎮 Games Collection - Python Implementation
A collection of two classic games implemented in Python: Cops and Robbers and Tic Tac Toe. This project was originally developed in C and converted to Python with enhanced user experience and intelligent AI.

✨ Features

Two Classic Games: Cops and Robbers strategy game and Tic Tac Toe
Smart AI: Intelligent computer opponents that adapt to your moves
User-Friendly Interface: Clear prompts and helpful error messages
Input Validation: Robust error handling for all user inputs
Customizable Board Size: Adjustable game board dimensions (Cops and Robbers)
Clean Code: Well-structured, documented Python code

🎯 Games
Cops and Robbers
A strategic chase game where cops try to catch a robber on a customizable grid.
Features:

Customizable board size (5x5 to 30x30)
1-5 cops controlled by the player
Smart robber AI that moves away from the closest cop
Cops can "wrap around" the board edges
30-move time limit

Objective: Catch the robber before 30 moves are completed!
Tic Tac Toe
The classic 3x3 grid game with an intelligent computer opponent.
Features:

Smart AI that tries to win and blocks player wins
Clear board visualization
Alternating turns (player first)
Win detection for rows, columns, and diagonals

Objective: Get three X's in a row before the computer gets three O's!


🚀 Installation

Clone the repository:
git clone https://github.com/yourusername/games-collection.git
cd games-collection

Run the game:
python games.py


Enter your name when prompted
Choose a game from the main menu:

1 - Cops and Robbers
2 - Tic Tac Toe
3 - Exit



Cops and Robbers Quick Start:

Choose board dimensions
Select number of cops (1-5)
Place cops on the board (avoid 3 in a row/column)
Move cops using direction keys: w(up), s(down), a(left), d(right)
Catch the robber before 30 moves!

Tic Tac Toe Quick Start:

Enter row and column (0-2) for your X
Computer automatically places O
First to get 3 in a row wins!

📖 Game Rules
Cops and Robbers Rules:

Board Setup: Choose rows and columns (5-30 each)
Robber Placement: Starts in center of the board
Cop Placement: No more than 2 cops in same row/column
Movement: Cops move one space per turn in 4 directions
Wrapping: Cops can move from one edge to the opposite edge
Robber AI: Moves away from closest cop automatically
Win Conditions:

Cops win: Catch the robber
Robber wins: Survive 30 moves



Tic Tac Toe Rules:

Standard 3x3 grid
Player: X (goes first)
Computer: O (smart AI)
Win Conditions: 3 in a row (horizontal, vertical, or diagonal)
Tie: Board full with no winner

🏗️ Code Structure
games.py
├── main()                    # Entry point
├── Games()                   # Main game loop and menu
├── SetNames()               # User name input
├── SetRows() / SetColumns() # Board size configuration
├── 
├── Cops and Robbers:
│   ├── CopsAndRobbers()     # Main game logic
│   ├── RobberMove()         # AI robber movement
│   └── PrintBoard()         # Board visualization
│
└── Tic Tac Toe:
    ├── TicTacToe()          # Main game logic
    ├── ComputerMoveTicTacToe() # Smart AI moves
    ├── FindWinningMove()    # Win/block detection
    ├── CheckWinner()        # Win condition checker
    └── PrintTicTacToeBoard() # Board display
