# Board 6x6
# def board():
#     print()
#     print("    | 1 | 2 | 3 | 4 | 5 | 6 | ")
#     # print("    ------------------------- ")
#     for i, row in enumerate(field):
#         row_str = f"  {i + 1} | {' | '.join(row)} | "
#         print(row_str)
#         # print("  --------------------------- ")

# Player and Computer
## Computer shoots randomly, not shooting twice the same spot
# Class Ship() inits with starting position


class Ship:
    def __init__(self, bow, l, o):
        self.bow = bow
        self.l = l
        self.o = o
        self.lives = l

    @property
    def dots(self):
        ship_dots = []
        for i in range(self.l):
            cur_x = self.bow.x
            cur_y = self.bow.y

            if self.o == 0:
                cur_x += i

            elif self.o == 1:
                cur_y += i

            ship_dots.append(Dot(cur_x, cur_y))

        return ship_dots

    def shooten(self, shot):
        return shot in self.dots
# Class Board()


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Dot({self.x}, {self.y})"


class BoardException(Exception):
    pass


class BoardOutException(BoardException):
    def __str__(self):
        return "Вы пытаетесь выстрелить за доску!"


class BoardUsedException(BoardException):
    def __str__(self):
        return "Вы уже стреляли в эту клетку"


class BoardWrongShipException(BoardException):
    pass

# My attempt
# class Board:
#     def __init__(self, side):
#         self.side = side
#
#     def print_side(self):
#         print(self.side)
#
#     def print_board(self):
#         print()
#         print("    | 1 | 2 | 3 | 4 | 5 | 6 | ")
#         # print("    ------------------------- ")
#         for i, row in enumerate(field):
#             row_str = f"  {i + 1} | {' | '.join(row)} | "
#             print(row_str)
#             # print("  --------------------------- ")


class Board:
    def __init__(self, field, starting_ships, hid, ships_left):
        self.field = field
        self.ships = starting_ships
        self.hid = hid
        self.ships_left = ships_left

    def add_ship(self):
        pass

    def contour(self):
        pass

    def out(self):
        pass

    def shot(self):
        pass
# Ships padded 1 empty spot
# Ships marked with ■
# Ships: 1 - 3 spots, 2 - 2 spots, 4 - 1 spot
# Player can't shoot the same spot twice


class Player:
    def __init__(self):
        self.own_board
        self.enemy_board

    def ask(self):
        pass

    def move(self):
        pass


class AI(Player):
    def ask(self):
        pass


class User(Player):
    def ask(self):
        pass


class Game:
    def __init__(self):
        pass

    def random_board(self):
        pass

    def greet(self):
        pass

    def loop(self):
        pass

    def start(self):
        pass
## Throw Exeption if he does
# Throw Exeptions when something unexpected happens
# X marks hits, T - misses, O - fog of war
# The one destroying all enemy ships wins


field = [[" "] * 6 for i in range(6)]
print(field)
game_board = Board(00, True, 10, 0)

# Printing on board
field[0][0] = 'T'
print(field[0][0])

my_dot = Dot(0, 0)
print(my_dot)
print(repr(my_dot))
