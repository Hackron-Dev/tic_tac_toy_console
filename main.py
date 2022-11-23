import random
# Console tic tac toy
board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]
currentPlayer = random.choice("X0")
winner = None
gameRunning = True
print("Welcome to Tic Tac Toy")

# computer
def computer(board):
    if currentPlayer == "0":
        position = random.randint(0,8)
        if board[position] == " ":
            board[position] = "0"
            switchPlayer()


# printing the game board
def printBoard(board):
    print(board[0] + " |", board[1] + " |", board[2])
    print("--+---+---")
    print(board[3] + " |", board[4] + " |", board[5])
    print("--+---+---")
    print(board[6] + " |", board[7] + " |", board[8])
    print("==========")


# printBoard(board)


# take pleyer input
def takePlayerInput(board):
    while currentPlayer != "0":
        inp = int(input("Enter a number 1-9: "))
        if 1 <= inp <= 9 and board[inp - 1] == " ":
            board[inp - 1] = currentPlayer
            switchPlayer()

        else:
            print("You cant go there!")


# check for win or tie
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != " ":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != " ":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != " ":
        winner = board[6]
        return True
    else:
        return False


def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != " ":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != " ":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != " ":
        winner = board[2]
        return True
    else:
        return False


def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != " ":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != " ":
        winner = board[2]
        return True
    else:
        return False

def checkTie(board):
    global gameRunning
    if " " not in board:
        printBoard(board)
        print("It's a tie!")
        gameRunning = False

# check for win
def checkWin():
    if checkDiag(board) or checkRow(board) or checkHorizontal(board):
        print(f"The winner is {winner}")
        printBoard(board)
        quit()



#switch the player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "0"
    else:
        currentPlayer = "X"

# run game
while gameRunning:
    printBoard(board)
    takePlayerInput(board)
    checkWin()
    checkTie(board)
    computer(board)
    checkWin()
    checkTie(board)