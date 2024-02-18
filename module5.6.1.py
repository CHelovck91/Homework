# Итоговое практическое задание, модуль B5
# ---------------------------------------------------
# Автор задания: Марушкевич Тимур Евгеньевич, #PDEV_49

# Зададим количество клеток игрового поля
board_size = 3

# Пронумеруем каждую клетку игрового поля
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def draw_board():
    '''Выводим игровое поле'''
    print('-' * 4 * board_size + '-')
    for i in range(board_size):
       # print((' ' * 3 + '|')*3)
        print('|', board[0 + i*board_size], '|', board[1 + i*board_size], '|', board[2 + i*board_size], '|')
        print('-' * 4 * board_size + '-')
    pass

def game_step(index, char):
    '''выполняем ход'''
    if (index > 10 or index < 1 or board[index-1] in ('X', 'O')):
        return False
    board[index - 1] = char
    return True

def check_win():
    '''Проверяем победил ли один из игроков'''
    win = False
    win_combo = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),    # горизонтальные линии
        (0, 3, 6), (1, 4, 7), (2, 5, 8),    # вертикальные линии
        (0, 4, 8), (2, 4, 6)                # диагональные линии
    )
    for pos in win_combo:
        if (board[pos[0]] == board[pos[1]] and board[pos[1]] == board[pos[2]]):
            win = board[pos[0]]
    return win

def start_game():
    # текущий игрок
    current_player = 'X'
    # номер шага
    step = 1
    draw_board()

    while (step<10) and (check_win() == False):
        index = input('Ходит игрок ' + current_player + '. Введите номер поля (0 - выход из игры):')

        if (index == '0'):
            break
        # если получилось сделать шаг
        if (game_step(int(index), current_player)):
            print('Удачный ход')
            if (current_player == 'X'):
                current_player = 'O'
            else:
                current_player = 'X'
            draw_board()
            # увеличим номер хода
            step += 1
        else:
            print('Неверный номер! Повторите!')
    if (step == 10):
        print('Игра окончена. Ничья!')
    else:
        print('Выиграл ' + check_win())

print('Добро пожаловать в крестики-нолики')
start_game()
