import math

# Global constants
MAX_SIZE = 30
MIN_SIZE = 5

# Global variables
first_name = ""
last_name = ""


def main():
    Games()
    return 0


def Games():
    SetNames()

    while True:
        print(
            f"Hello {first_name} {last_name}, what would you like to play? (1) Cops and Robbers (2) Tic tac toe (3) Exit")
        print("Please enter your choice (1, 2, or 3): ", end="")

        try:
            choice = int(input())
            if choice == 1:
                CopsAndRobbers()
            elif choice == 2:
                TicTacToe()
            elif choice == 3:
                print(f"Bye, {first_name} {last_name}.")
                break
            else:
                print("Invalid choice! Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input! Please enter a number (1, 2, or 3).")


def SetNames():
    global first_name, last_name

    print("Enter first name")
    print("Please type your first name and press Enter: ", end="")
    first_name = input().strip()

    print("Enter last name")
    print("Please type your last name and press Enter: ", end="")
    last_name = input().strip()


def SetRows():
    print(f"Enter number of rows (minimum {MIN_SIZE}, maximum {MAX_SIZE}): ", end="")
    rows = int(input())

    if rows > MAX_SIZE:
        rows = MAX_SIZE
        print(f"Too large! Setting to maximum: {MAX_SIZE}")
    elif rows < MIN_SIZE:
        rows = MIN_SIZE
        print(f"Too small! Setting to minimum: {MIN_SIZE}")

    return rows


def SetColumns(rows_value):
    print(f"Enter number of columns (minimum {MIN_SIZE}, maximum {MAX_SIZE}, or -1 to use same as rows): ", end="")
    columns = int(input())

    if columns == -1:
        columns = rows_value
        print(f"Using same as rows: {columns}")
    elif columns > MAX_SIZE:
        columns = MAX_SIZE
        print(f"Too large! Setting to maximum: {MAX_SIZE}")
    elif columns < MIN_SIZE:
        columns = MIN_SIZE
        print(f"Too small! Setting to minimum: {MIN_SIZE}")

    return columns


def PrintBoard(board, rows, cols):
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 0:
                print("-", end="")
            elif board[i][j] == 1:  # Robber
                print("R", end="")
            elif board[i][j] == 2:  # Cop
                print("C", end="")
        print()


def CopsAndRobbers():
    print("Let's choose the size:")
    rows = SetRows()
    cols = SetColumns(rows)

    # Initialize board
    board = [[0 for _ in range(cols)] for _ in range(rows)]

    # Place robber in center (or as close as possible)
    robber_row = (rows - 1) // 2
    robber_col = (cols - 1) // 2

    # Adjust robber position based on assignment requirements
    if rows >= 4 and cols >= 3:
        robber_row = 3
        robber_col = 2
    if robber_row >= rows:
        robber_row = rows - 1
    if robber_col >= cols:
        robber_col = cols - 1

    board[robber_row][robber_col] = 1

    # Get number of cops
    print("How many cops would you like (1-5)?")
    num_cops = int(input())

    cop_positions = []

    # Place cops
    for i in range(num_cops):
        while True:
            print("Let's choose cells:")
            print(f"Enter position for cop #{i + 1}")
            print("Row (0 to {}): ".format(rows - 1), end="")
            try:
                cop_row = int(input())
                print("Column (0 to {}): ".format(cols - 1), end="")
                cop_col = int(input())

                # Check if position is valid
                if (cop_row < 0 or cop_row >= rows or
                        cop_col < 0 or cop_col >= cols):
                    print("Illegal choice! Position out of bounds.")
                    continue

                if board[cop_row][cop_col] != 0:
                    print("Illegal choice! Position already occupied.")
                    continue

                # Check for three cops in a row/column
                valid_placement = True

                # Check row
                row_count = sum(1 for c in range(cols) if board[cop_row][c] == 2)
                if row_count >= 2:
                    print("Illegal choice! Too many cops in this row.")
                    valid_placement = False

                # Check column
                col_count = sum(1 for r in range(rows) if board[r][cop_col] == 2)
                if col_count >= 2:
                    print("Illegal choice! Too many cops in this column.")
                    valid_placement = False

                if not valid_placement:
                    continue

                board[cop_row][cop_col] = 2
                cop_positions.append((cop_row, cop_col))
                break

            except (ValueError, IndexError):
                print("Illegal choice! Please enter valid numbers.")

    print("Let's play!")
    print("Initial states:")
    PrintBoard(board, rows, cols)
    print()

    moves = 0
    max_moves = 30

    while moves < max_moves:
        # Cops turn
        print("Cops:")

        # Show possible moves
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 2:
                    moves_list = []
                    # Check up
                    if i > 0 and board[i - 1][j] != 2:
                        moves_list.append("up(w)")
                    # Check down
                    if i < rows - 1 and board[i + 1][j] != 2:
                        moves_list.append("down(s)")
                    # Check left
                    if j > 0 and board[i][j - 1] != 2:
                        moves_list.append("left(a)")
                    # Check right
                    if j < cols - 1 and board[i][j + 1] != 2:
                        moves_list.append("right(d)")

                    # Handle wrapping
                    if board[i][(j - 1) % cols] != 2:
                        if "left(a)" not in moves_list:
                            moves_list.append("left(a)")
                    if board[i][(j + 1) % cols] != 2:
                        if "right(d)" not in moves_list:
                            moves_list.append("right(d)")

                    if moves_list:
                        print(f"Cop [{i}, {j}] can move: {' '.join(moves_list)}")

        print("Select a cop[row,col] and a direction")
        print("Enter the cop's current row: ", end="")

        try:
            cop_row = int(input())
            print("Enter the cop's current column: ", end="")
            cop_col = int(input())
            print("Enter direction (w=up, s=down, a=left, d=right): ", end="")
            direction = input().strip()

            # Validate cop position
            if (cop_row < 0 or cop_row >= rows or
                    cop_col < 0 or cop_col >= cols or
                    board[cop_row][cop_col] != 2):
                print("You lose your turn - Invalid cop position!")
                moves += 1
                continue

            # Move cop based on direction
            new_row, new_col = cop_row, cop_col

            if direction == 'w':  # up
                new_row = cop_row - 1
                if new_row < 0:
                    new_row = rows - 1
            elif direction == 's':  # down
                new_row = cop_row + 1
                if new_row >= rows:
                    new_row = 0
            elif direction == 'a':  # left
                new_col = (cop_col - 1) % cols
            elif direction == 'd':  # right
                new_col = (cop_col + 1) % cols
            else:
                print("You lose your turn - Invalid direction! Use w, s, a, or d.")
                moves += 1
                continue

            # Check if move is valid (not occupied by another cop)
            if board[new_row][new_col] == 2:
                print("You lose your turn - Cannot move to a position occupied by another cop!")
                moves += 1
                continue

            # Check if cop caught robber
            if board[new_row][new_col] == 1:
                board[cop_row][cop_col] = 0
                board[new_row][new_col] = 2
                PrintBoard(board, rows, cols)
                print()
                print("The cops won!")
                return

            # Move cop
            board[cop_row][cop_col] = 0
            board[new_row][new_col] = 2

        except (ValueError, IndexError):
            print("You lose your turn - Invalid input! Please enter numbers for position and a letter for direction.")
            moves += 1
            continue

        PrintBoard(board, rows, cols)
        print()

        moves += 1

        # Robber's turn
        robber_moved = RobberMove(board, rows, cols, robber_row, robber_col)
        if robber_moved:
            robber_row, robber_col = robber_moved

        PrintBoard(board, rows, cols)
        print()

    print("The robber managed to escape!")


def RobberMove(board, rows, cols, robber_row, robber_col):
    # Find closest cop
    min_distance = float('inf')
    closest_cop = None

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 2:
                distance = math.sqrt((robber_row - i) ** 2 + (robber_col - j) ** 2)
                if (distance < min_distance or
                        (distance == min_distance and
                         (i < closest_cop[0] or (i == closest_cop[0] and j < closest_cop[1])))):
                    min_distance = distance
                    closest_cop = (i, j)

    if not closest_cop:
        return None

    # Try moves in priority order: up, down, left, right
    moves = [
        (robber_row - 1, robber_col),  # up
        (robber_row + 1, robber_col),  # down
        (robber_row, robber_col - 1),  # left
        (robber_row, robber_col + 1)  # right
    ]

    best_move = None
    max_distance = -1

    for new_row, new_col in moves:
        # Check bounds
        if (new_row < 0 or new_row >= rows or
                new_col < 0 or new_col >= cols or
                board[new_row][new_col] == 2):
            continue

        # Calculate distance to closest cop
        distance = math.sqrt((new_row - closest_cop[0]) ** 2 + (new_col - closest_cop[1]) ** 2)

        if distance > max_distance:
            max_distance = distance
            best_move = (new_row, new_col)

    if best_move:
        board[robber_row][robber_col] = 0
        board[best_move[0]][best_move[1]] = 1
        return best_move

    return (robber_row, robber_col)


def TicTacToe():
    board = [['-' for _ in range(3)] for _ in range(3)]
    PrintTicTacToeBoard(board)

    computer_start = 1  # Computer starts from position 1

    for turn in range(9):
        if turn % 2 == 0:  # User's turn
            print("Select a square (row, col)")
            print("Enter row (0, 1, or 2): ", end="")
            try:
                row = int(input())
                print("Enter column (0, 1, or 2): ", end="")
                col = int(input())

                if row < 0 or row > 2 or col < 0 or col > 2:
                    print("Outside of board")
                    continue

                if board[row][col] != '-':
                    print("Invalid square")
                    continue

                board[row][col] = 'X'

            except ValueError:
                print("Invalid input - Please enter numbers only!")
                continue

        else:  # Computer's turn
            print("Computer's turn")
            print()

            moved = ComputerMoveTicTacToe(board, computer_start)
            computer_start = (computer_start % 9) + 1  # Next starting position

            if not moved:
                break

        PrintTicTacToeBoard(board)

        # Check for win
        winner = CheckWinner(board)
        if winner == 'X':
            print(f"{first_name}, {last_name} has won!")
            return
        elif winner == 'O':
            print(f"{first_name}, {last_name} has lost!")
            return
        elif IsBoardFull(board):
            print("It was a tie!")
            return


def ComputerMoveTicTacToe(board, start_pos):
    """Computer makes a smart move in Tic Tac Toe"""

    # First priority: Try to win (if computer has 2 in a row)
    win_move = FindWinningMove(board, 'O')
    if win_move:
        row, col = win_move
        board[row][col] = 'O'
        return True

    # Second priority: Block player from winning (if player has 2 in a row)
    block_move = FindWinningMove(board, 'X')
    if block_move:
        row, col = block_move
        board[row][col] = 'O'
        return True

    # Third priority: Use the original algorithm (cycle through positions)
    # Position mapping (1-9 to row,col)
    positions = [
        (0, 0), (0, 1), (0, 2),  # 1, 2, 3
        (1, 0), (1, 1), (1, 2),  # 4, 5, 6
        (2, 0), (2, 1), (2, 2)  # 7, 8, 9
    ]

    # Start from the specified position and wrap around
    for i in range(9):
        pos_index = (start_pos - 1 + i) % 9
        row, col = positions[pos_index]

        if board[row][col] == '-':
            board[row][col] = 'O'
            return True

    return False


def FindWinningMove(board, player):

    # Check all empty positions
    for row in range(3):
        for col in range(3):
            if board[row][col] == '-':
                # Temporarily place the player's symbol
                board[row][col] = player

                # Check if this creates a win
                if CheckWinner(board) == player:
                    board[row][col] = '-'  # Restore the empty space
                    return (row, col)

                board[row][col] = '-'  # Restore the empty space

    return None


def PrintTicTacToeBoard(board):
    for row in board:
        print(''.join(row))


def CheckWinner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != '-':
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '-':
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '-':
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '-':
        return board[0][2]

    return None


def IsBoardFull(board):
    for row in board:
        for cell in row:
            if cell == '-':
                return False
    return True


if __name__ == "__main__":
    main()
