# enemies = 1
# print(enemies)
#
#
# def increase_enemies():
# 	return enemies + 1
#
#
# enemies = increase_enemies()
# print(enemies)

x_score = 0


def x_won():
	x_score = x_score + 1


while True:
	global x_score
	user = input()
	x_score = x_won()
	x_score
	print(x_score)
