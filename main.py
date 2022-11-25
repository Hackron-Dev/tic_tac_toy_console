import random

board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

player = random.choice("X0")
if player == "0":
    computer = 'X'
    PlayerStep = False
else:
    computer = "0"
    PlayerStep = True


def switchPlayer():
    global PlayerStep
    if PlayerStep:
        PlayerStep = False
    else:
        PlayerStep = True


def printBoard(board):
    print(board[1] + "|" + board[2] + "|" + board[3])
    print("-+-+-")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-+-+-")
    print(board[7] + "|" + board[8] + "|" + board[9])
    print("\n")


printBoard(board)


def spaceIsFree(position):
    if board[position] == ' ':
        return True
    return False


def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        printBoard(board)
        if checkDraw():
            print("Draw!")
            exit()
        if checkWin():
            if letter == 'X':
                print("Bot wins!")
                exit()
            else:
                print("Player wins!")
                exit()
        return
    else:
        print("Invalid position")
        position = int(input("Please enter a new position: "))
        insertLetter(letter, position)
        return


def checkWin():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False


def checkWhichMarkWon(mark):
    if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
        return True
    elif board[4] == board[5] and board[4] == board[6] and board[4] == mark:
        return True
    elif board[7] == board[8] and board[7] == board[9] and board[7] == mark:
        return True
    elif board[1] == board[4] and board[1] == board[7] and board[1] == mark:
        return True
    elif board[2] == board[5] and board[2] == board[8] and board[2] == mark:
        return True
    elif board[3] == board[6] and board[3] == board[9] and board[3] == mark:
        return True
    elif board[1] == board[5] and board[1] == board[9] and board[1] == mark:
        return True
    elif board[7] == board[5] and board[7] == board[3] and board[7] == mark:
        return True
    else:
        return False


def checkDraw():
    for key in board.keys():
        if board[key] == ' ':
            return False
    return True


def playerMove():
    if PlayerStep == True:
        position = int(input(f"Enter a position for '{player}': "))
        insertLetter(player, position)
        switchPlayer()
        return


def compMove():
    if PlayerStep == False:
        bestScore = -800  # Изначально мы берем худший ход как лучший чтоб если ничего кроме худшего хода не осталось мы сходили именно худшим
        bestMove = 0
        for key in board.keys():  # проходимся по словарю (полю)
            if board[key] == ' ':  # если клетка пустая
                board[key] = computer  # компьютер подставляет свой ход на клетку
                score = minimax(board, False)  # и смотрит что у него получилось
                board[key] = ' '  # потом мы очищаем эту клетку
                if score > bestScore:  # и если значение больше лучшего значения
                    bestScore = score  # мы приравниваем лучшее значение к значению
                    bestMove = key  # тут храниться расположение лучшего хода
        insertLetter(computer, bestMove)  # тут мы говорим что он выбирает лучший ход
        switchPlayer()  # меням очередь
        return


def minimax(board, isMaximizing):
    if checkWhichMarkWon(computer):  # в этом блоке кода мы проверяем чей ход будет победным и говорим
        return 1  # если ход компьютера, то даем ему бал
    elif checkWhichMarkWon(player):
        return -1  # Если человека, забераем балл
    elif checkDraw():
        return 0  # Если ничья, то ничего не меняем

    if isMaximizing: # Тут идет проверка для компьютера
        bestScore = -800
        for key in board.keys():
            if board[key] == ' ':
                board[key] = computer
                score = minimax(board, False)
                board[key] = ' '
                if score > bestScore:
                    bestScore = score
        return bestScore
    else: # Тут идет проверка для Игрока
        bestScore = 800 # Мы пытаемся найти худший ход для игрока
        for key in board.keys(): # проходимся по словарю (полю)
            if board[key] == ' ': # если клетка пустая
                board[key] = player # игрок подставляет свой ход на клетку
                score = minimax(board, True) # и мы проверяем что у него получилось
                board[key] = ' ' # потом мы очищаем эту клетку
                if score < bestScore: # и если значение меньше лучшего значения
                    bestScore = score # мы приравниваем лучшее значение к значению
        return bestScore


while not checkWin():
    compMove()
    playerMove()
