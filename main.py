
print(f"Приветсвую вас в игре КРЕСТИКИ НОЛИКИ!!!!\n"
      f"В игре принимают участие два игрока")
player_1 = input("Игрок №1 (крестики) введите свое имя: ")
player_2 = input("Игрок №2 (нолики) введите свое имя: ")

EMPTY = ' '
players = ['X','O']
current_player = 0

def create_board():
    board = []
    for _ in range(3):
        row = [EMPTY] * 3
        board.append(row)
    return board


def display_board(board):
    for row in board:
        print('|'.join(row))
        print('_'*5)


board = create_board()
while True:
    if current_player == 0:
        print(f'{player_1} ходит')
    elif current_player == 1:
        print(f'{player_2} ходит')
    row = int(input('Введите номер строки(0-2)'))
    col = int(input('Введите номер столбца(0-2)'))


    player = players[current_player]
    board[row][col] = player
    display_board(board)
    current_player = 1 - current_player



