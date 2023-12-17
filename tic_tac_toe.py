import random, math, os, time

score = [0, 0, 0]
state_message = ["You won!","You lost!","It's a tie!"]
player = "X"
computer = "O"

def draw_board():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"\
         |     |     \n\
      {board[0][0]}  |  {board[0][1]}  |  {board[0][2]}  \n\
    _____|_____|_____\n\
         |     |     \n\
      {board[1][0]}  |  {board[1][1]}  |  {board[1][2]}  \n\
    _____|_____|_____\n\
         |     |     \n\
      {board[2][0]}  |  {board[2][1]}  |  {board[2][2]}  \n\
         |     |     \n\
Wins: {score[0]} Losses: {score[1]} Ties: {score[2]}")
    
def game_turn(n):
    if n == 1:
        computer_turn()
    else:
        player_turn()

def player_turn():
    while True:
        try:
            player_move = int(input("Enter 1-9 to make a move or 0 to quit: "))
            if player_move == 0:
                print("Thanks for playing!")
                quit()
            if player_move in range(1,10):
                y = math.ceil(player_move / 3) - 1
                x = player_move % 3 - 1
                if board[y][x] != player and board[y][x] != computer:
                    board[y][x] = player                    
                    draw_board()
                    break
        except ValueError:
            pass
        print ("\033[A                                                                       \033[A")
        print("Not a valid move!".center(25,"-"))   

def computer_turn():
    time.sleep(1)
    while True:
        computer_move = random.randint(1,9)
        y = math.ceil(computer_move / 3) - 1
        x = computer_move % 3 - 1
        if board[y][x] != player and board[y][x] != computer:
            board[y][x] = computer
            draw_board()
            break


def check_state(board):
    # Check all horizontal rows
    board_values = set()
    for i in range(3):
        for j in range(3):
            board_values.add(board[i][j])
        if board_values == {player}:
            return 0
        elif board_values == {computer}:
            return 1
        else:
            board_values.clear()
        
    # Check all vertical rows
    for i in range(3):
        for j in range(3):
            board_values.add(board[j][i])
        if board_values == {player}:
            return 0
        elif board_values == {computer}:
            return 1
        else:
            board_values.clear()
    
    # Check the 2 diagonals
    for i in range (3):
        board_values.add(board[i][i])
    if board_values == {player}:
        return 0
    elif board_values == {computer}:
        return 1
    else:
        board_values.clear()

    for i in range (3):
        board_values.add(board[i][2-i])
    if board_values == {player}:
        return 0
    elif board_values == {computer}:
        return 1
    else:
        board_values.clear()

    # Check if there is a tie/board is full -> return 2
    if moves == 9:
        return 2

while True:
    turn = random.randint(0, 1)
    moves = 0
    board = [["1","2","3"],["4","5","6"],["7","8","9"]]
    draw_board()
    while True: 
        game_turn(turn)
        turn = 1 - turn
        moves += 1
        state = check_state(board)
        if state in [0, 1, 2]:
            score[state] += 1
            draw_board()
            print(state_message[state].center(25,"-"))
            time.sleep(3)
            break

