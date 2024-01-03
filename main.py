
print(f"Приветсвую вас в игре КРЕСТИКИ НОЛИКИ!!!!\n"
      f"В игре принимают участие два игрока")
player_1 = input("Игрок №1 (крестики) введите свое имя: ")
player_2 = input("Игрок №2 (нолики) введите свое имя: ")

EMPTY = ' '
players = ['X','O']
current_player = 0


# создание поля
def create_board():
    board = []
    for _ in range(3):
        row = [EMPTY] * 3
        board.append(row)
    return board


# отображение поля
def display_board(board):
    for row in board:
        print('|'.join(row))
        print('_'*5)


# Проверка на победу
def win_chekin(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None


board = create_board()
# цикл игры
while True:
    if current_player == 0:
        print(f'{player_1} ходит')
    elif current_player == 1:
        print(f'{player_2} ходит')
    row = int(input('Введите номер строки(0-2)'))
    col = int(input('Введите номер столбца(0-2)'))
    player = players[current_player]
    if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != EMPTY:
        print("Некорректный ход. Попробуйте еще раз.")
    else:
        board[row][col] = player
        current_player = 1 - current_player
    display_board(board)
    winner = win_chekin(board)
    if winner == 'X':
        print(f"Победитель {player_1}")
        break
    if winner == 'O':
        print(f"Победитель {player_2}")
        break
    if all(board[row][col] != EMPTY for row in range(3) for col in range(3)):
        print("Победила дружба!!!")
        break




