# Console tic tac toy
board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_"]
currentPlayer = "X"
winner = None
gameRunning = True
print("Welcome to Tic Tac Toy")


# printing the game board
def printBoard(board):
    print(board[0] + " |", board[1] + " |", board[2])
    print("-----------")
    print(board[3] + " |", board[4] + " |", board[5])
    print("-----------")
    print(board[6] + " |", board[7] + " |", board[8])


#printBoard(board)


# take pleyer input
def takePlayerInput(board):
    inp = int(input("Enter a number 1-9: "))
    if 1 <= inp <= 9 and board[inp - 1] == "_":
        board[inp-1] = currentPlayer
    else:
        print("You cant go there!")

# check for win or tie


while gameRunning:
    printBoard(board)
    takePlayerInput(board)

