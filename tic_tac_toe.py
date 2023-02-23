import sys
print ("Tic Tac Toe Game")

# 1D arrat to stoare the game board

board = ["-"]*9
player = 0 

def check_if_won(player):
    
    if board[0] == player and board[1] == player and board[2] == player:
        return True
    elif board[3] == player and board[4] == player and board[5] == player:
        return True
    elif board[6] == player and board[7] == player and board[8] == player:
        return True
    elif board[0] == player and board[3] == player and board[6] == player:
        return True
    elif board[1] == player and board[4] == player and board[7] == player:
        return True
    elif board[2] == player and board[5] == player and board[8] == player:
        return True
    elif board[0] == player and board[4] == player and board[8] == player:
        return True
    elif board[2] == player and board[4] == player and board[6] == player:
        return True
    return False

def display_board():
    #TODO: write code to display board
    i=0
    while i < 9:
        print("{} {} {}".format( board[i], board[i+1] , board[i+2]))
        i =i+3

display_board()

for i in range(9):
    # take input from player
    if player == 0:
        #take input from player A
        position = input('Player 0, please enter position: ')
        board[int(position)] = player
        display_board()
        #Check if player A won the game
        result = check_if_won(player)
        if result == True:
            print("Player 0 won the Game!")
            sys.exit()
        else:
            player = 1

    else:
        #take input from player B
        position = input('Player 1, please enter position: ')
        board[int(position)] = player
        display_board()
        #Check if player A won the game
        result = check_if_won(player)
        if result == True:
            print("Player 1 won the Game!")
            sys.exit()
        else:
            player = 0

print("Noboday won the game. :(")