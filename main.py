from game import draw_board, board, check_winner, check_draw, player_input

def play_game():
    """Main game loop"""
    print("="*20)
    print("Welcome to Tic Tac Toe!")
    print("="*20)
    
    current_player = 'X'
    game_over = False
    
    while not game_over:
        draw_board(board)
        player_input(board, current_player)
        
        if check_winner(board, current_player):
            draw_board(board)
            print(f"🎉 Player {current_player} wins! Congratulations!")
            game_over = True
        elif check_draw(board):
            draw_board(board)
            print("🤝 It's a draw!")
            game_over = True
        else:
            # Switch player
            current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_game()
    print("Thanks for playing!")
