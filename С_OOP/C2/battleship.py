# TODO Board 6x6
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
    def __init__(self):
        pass # TODO generate starting positions
# Class Board()
class Board:
    def __init__(self, side):
        self.side = side

    def print_side(self):
        print(self.side)

    def print_board(self):
        print()
        print("    | 1 | 2 | 3 | 4 | 5 | 6 | ")
        # print("    ------------------------- ")
        for i, row in enumerate(field):
            row_str = f"  {i + 1} | {' | '.join(row)} | "
            print(row_str)
            # print("  --------------------------- ")

# Ships padded 1 empty spot
# Ships marked with ■
# Ships: 1 - 3 spots, 2 - 2 spots, 4 - 1 spot
# Player can't shoot the same spot twice
## Throw Exeption if he does
# Throw Exeptions when something unexpected happens
# X marks hits, T - misses, O - fog of war
# The one destroying all enemy ships wins


field = [[" "] * 6 for i in range(6)]
print(field)
game_board = Board('Player')
game_board.print_board()
# Printing on board
field[0][0] = 'T'
print(field)

game_board.print_board()
