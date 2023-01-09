#Tic tac toe/ Piškorky

# 1. Vytvořte funkci, která vytvoří hrací pole pro hru Tic Tac Toe.
# 2. Funkce bude mít jeden parametr, který bude určovat velikost hracího pole.
# 3. Funkce bude vracet hrací pole jako dvourozměrné pole.
# 4. Vytvořte funkci, která vypíše hrací pole na obrazovku.
# 5. Vytvořte funkci, která bude zjišťovat, zda je hrací pole plné.
# 6. Vytvořte funkci, která bude zjišťovat, zda je hráč vyhrál.
# 7. Vytvořte funkci, která bude zjišťovat, zda je hráč prohrál.
# 8. Vytvořte funkci, která bude zjišťovat, zda je hra remíza.
# 9. Vytvořte funkci, která bude zjišťovat, zda je hra dokončena.
# 10. Vytvořte funkci, která bude zjišťovat, zda je tah možný.

import random #importuje modul random

def create_board(size): #vytvori hraci pole
    board = [] #vytvori prazdne pole
    for i in range(size): #cyklus pro vytvoreni pole
        board.append([])
        for j in range(size):
            board[i].append(" ") #prida mezery do pole
    return board 

def print_board(board): #vypise hraci pole
    for i in range(len(board)):
        print(" ---" * len(board), end="") 
        print()
        print("|", end="") 
        for j in range(len(board)):
            print(" " + board[i][j] + " |", end="")
        print()
    print(" ---" * len(board), end="")
    print()

def is_board_full(board): #zjisti, zda je hraci pole plne
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == " ":
                return False
    return True

def is_winner(board, player): #zjisti, zda je hrac vyhral
    # Check horizontal
    for i in range(len(board)):
        win = True
        for j in range(len(board)):
            if board[i][j] != player:
                win = False
                break
        if win == True:
            return True
    # Check vertical
    for i in range(len(board)): 
        win = True
        for j in range(len(board)):
            if board[j][i] != player:
                win = False
                break
        if win == True:
            return True
    # Check diagonal
    win = True
    for i in range(len(board)):
        if board[i][i] != player:
            win = False
            break
    if win == True:
        return True
    # Check diagonal
    win = True
    for i in range(len(board)):
        if board[i][len(board) - 1 - i] != player:
            win = False
            break
    if win == True:
        return True
    return False

def is_tie(board): #zjisti, zda je hra remiza
    return is_board_full(board) and not(is_winner(board, "X")) and not(is_winner(board, "O"))

def is_game_over(board): #zjisti, zda je hra dokoncena
    return is_board_full(board) or is_winner(board, "X") or is_winner(board, "O")

def is_move_possible(board, row, col): #zjisti, zda je tah mozny
    if row < 0 or row >= len(board) or col < 0 or col >= len(board):
        return False
    if board[row][col] != " ":
        return False
    return True

def get_player_move(board): #zjisti tah hrace
    while True:
        row = int(input("Zadej řádek: "))
        col = int(input("Zadej sloupec: "))
        if is_move_possible(board, row, col):
            return row, col
        else:
            print("Tento pohyb nelze. Zkus zadat znovu")

def get_computer_move(board): #zjisti tah pocitace
    while True:
        row = random.randint(0, len(board) - 1)
        col = random.randint(0, len(board) - 1)
        if is_move_possible(board, row, col):
            return row, col

def play_game(): #hraje hru
    board = create_board(3)
    print_board(board)
    while True:
        row, col = get_player_move(board)
        board[row][col] = "X"
        print_board(board)
        if is_game_over(board):
            break
        row, col = get_computer_move(board)
        board[row][col] = "O"
        print_board(board)
        if is_game_over(board):
            break
    if is_winner(board, "X"):
        print("Vyhrál jsi!")
    elif is_winner(board, "O"):
        print("Vyhrál počítač!")
    else:
        print("Remíza!")

play_game() #spusti hru


