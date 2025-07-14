def main():
    board = [["1","2","3"], ["4","5","6"], ["7","8","9"]]
    player1 = "X"
    player2 = "O"
    winner = None
    free_spaces = ["1","2","3","4","5","6","7","8","9"]
    current_player = player1
    
    while winner is None:
        current_move = get_player_move(current_player, free_spaces)
        make_player_move(board, current_player, current_move)
        print_board(board)
        winner = check_winner(board)
        if winner is not None:
            print(f'Player{winner} wins!')
            break
        if len(free_spaces) == 0:
            print("It's a tie.")
            break
        
        if current_player == player1:
            current_player = player2
        else:
            current_player = player1
        

    
def print_board(board):
    for i in range(3):
        print(f" {board[i][0]} | {board[i][1]} | {board[i][2]}")
        if i < 2:
            print("---+---+---")
            
def get_player_move(player, free_spaces): #returns an int 1-9
    choice = input(f"Player {player}, enter a number(1-9): ").strip()
    while choice not in free_spaces:
        choice = input("Invalid choice. Please enter a number from 1-9: ").strip()
    free_spaces.remove(choice)
    return int(choice)

def make_player_move(board, player, move):
    row = ((move - 1) // 3)
    column = ((move - 1) % 3)
    
    board[row][column] = player
    
def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return None

main()