from os import system, name


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def greet():
    logo = """
 _   _        _               _             
| | (_)      | |             | |            
| |_ _  ___  | |_ __ _  ___  | |_ ___   ___ 
| __| |/ __| | __/ _` |/ __| | __/ _ \ / _ \\
| |_| | (__  | || (_| | (__  | || (_) |  __/
 \__|_|\___|  \__\__,_|\___|  \__\___/ \___|
 """
    print(logo)


def board():
    print()
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  ---------------")
    print()


def user_turn():
    while True:
        user_input = input("\tВаш ход: ").split()

        if len(user_input) != 2:
            print("Введите 2 координаты!")
            continue

        if not (user_input[0].isdigit()) or not (user_input[1].isdigit()):
            print("Введите числа!")
            continue

        x, y = map(int, user_input)

        if not (0 <= x < 3 and 0 <= y < 3):
            print("Координаты вне диапазона!")
            continue

        if field[x][y] != " ":
            print("Клетка занята! ")
            continue

        return x, y


def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False


greet()
game_on = True
while game_on:
    field = [[" "] * 3 for i in range(3)]
    print(field)
    count = 0
    while True:
        count += 1
        board()
        if count % 2 == 1:
            print("Ходит крестик!")
        else:
            print("Ходит нолик!")

        x, y = user_turn()

        if count % 2 == 1:
            field[x][y] = "X"
        else:
            field[x][y] = "0"

        if check_win():
            break

        if count == 9:
            print("Ничья!")
            break

    restart = input("Чтобы сыграть ещё, нажмите 1: ")
    if restart != "1":
        print("Спасибо за игру!")
        game_on = False

    clear()
