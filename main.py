import random
import os


def is_game_draw(field):
    if not is_game_winned(field):
        if '*' not in field[0] and '*' not in field[1] and '*' not in field[2]:
            return True
        else:
            return False


def is_move_available(field, move):
    if field[int(move[0])][int(move[1])] == '*':
        return True
    else:
        return False


def switch_who_is_move(who_is_move):
    if who_is_move == 'x':
        who_is_move = '0'
    else:
        who_is_move = 'x'

    return who_is_move


def player_way(field, user_side):
    print('Введите ваш ход в формате двух слитных чисел (ряд и колонка)')
    while True:
        try:
            user_move = input('Ход:')
            if len(user_move) == 2 and is_move_available(field, user_move):
                field[int(user_move[0])][int(user_move[1])] = user_side
                return field
            else:
                print("Ход невозможен. Введите другой ход:")
        except IndexError:
            print("Некорректный ввод.")

def computer_way(field, computer_side):
    available_ways = []

    for i in range(0, len(field)):
        for k in range(0, len(field[i])):
            if is_move_available(field, str(i) + str(k)):
                available_ways.append(f'{str(i) + str(k)}')
    choosed_way = random.randint(0, len(available_ways) - 1)

    field[int(available_ways[choosed_way][0])][int(available_ways[choosed_way][1])] = computer_side
    return field


def is_game_winned(field):
    if field[0][0] == field[0][1] == field[0][2] != '*' or field[1][0] == field[1][1] == field[1][2] != '*' or \
            field[2][0] == field[2][1] == field[2][2] != '*' or field[0][0] == field[1][0] == field[2][0] != '*' or \
            field[0][1] == field[1][1] == field[2][1] != '*' or field[0][2] == field[1][2] == field[2][2] != '*' or \
            field[0][0] == field[1][1] == field[2][2] != '*' or field[0][2] == field[1][1] == field[2][0] != '*':
        return True

    else:
        return False


def game(field, mode, user_side=''):
    who_is_move = 'x'
    while not is_game_winned(field) and not is_game_draw(field):
        show_field(field)
        if mode == 'PVP':
            field = player_way(field, who_is_move)
            who_is_move = switch_who_is_move(who_is_move)

        elif mode == 'PVC':
            if user_side == who_is_move:
                field = player_way(field, who_is_move)
                who_is_move = switch_who_is_move(who_is_move)

            else:
                field = computer_way(field, who_is_move)
                who_is_move = switch_who_is_move(who_is_move)

    show_field(field)
    if not is_game_draw(field):
        if who_is_move == 'x':
            print("Победили нолики!")

        else:
            print("Победили крестики!")

    else:
        print('Ничья!')


def choose_your_mode():
    user_mode = None
    while user_mode != '1' or user_mode != '2':
        print("Выберите ваш режим:")
        print('1 - С другим игроком', '2 - Против компьютера')
        user_mode = input('Ваш выбор:')
        if user_mode == '1':
            user_mode = 'PVP'
            os.system('cls' if os.name == 'nt' else 'clear')
            return user_mode

        elif user_mode == '2':
            user_mode = "PVC"
            os.system('cls' if os.name == 'nt' else 'clear')
            return user_mode

        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Некорректный ввод. Попробуйте снова.')


def choose_your_side():
    user_side = None
    while user_side != 'x' or user_side != '0':
        print("За кого будете играть?")
        print('x - крестики', '0 - нолики')
        user_side = input('Ваш выбор:')
        if user_side == '0' or user_side == 'x':
            os.system('cls' if os.name == 'nt' else 'clear')
            return user_side
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Некорректный ввод. Попробуйте снова.')


def show_field(field):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(field[0])
    print(field[1])
    print(field[2])


def main():
    field = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
    game_mode = choose_your_mode()
    player_side = None

    if game_mode == 'PVC':
        player_side = choose_your_side()

    game(field, game_mode, player_side)


if __name__ == "__main__":
    main()
