board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def draw_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("---+---+---")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("---+---+---")
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()

def check_winner(board, player):
    """Check if the current player has won"""
    win_conditions = [
        [0, 1, 2],  # Top row
        [3, 4, 5],  # Middle row
        [6, 7, 8],  # Bottom row
        [0, 3, 6],  # Left column
        [1, 4, 7],  # Middle column
        [2, 5, 8],  # Right column
        [0, 4, 8],  # Diagonal
        [2, 4, 6]   # Anti-diagonal
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def check_draw(board):
    """Check if the board is full (draw)"""
    return all(pos in ['X', 'O'] for pos in board)

def player_input(board, player):
    """Get player input and update board"""
    while True:
        try:
            pos = int(input(f"Player {player}, enter position (1-9): ")) - 1
            if pos < 0 or pos > 8:
                print("Invalid! Enter a number between 1-9.")
                continue
            if board[pos] in ['X', 'O']:
                print("Position already taken! Choose another.")
                continue
            board[pos] = player
            break
        except ValueError:
            print("Invalid input! Please enter a number.")
