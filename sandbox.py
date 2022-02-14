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

x_score = 1


# def x_won():
# 	global x_score
# 	x_score = x_score + 1
# 	return x_score
#
#
# while x_score < 5:
# 	user = int(input(": "))
# 	if user == 3:
# 		x_score = x_won()
# 	print(x_score)

def x_won():
	user = int(input(": "))
	return user


game_on = True

while game_on:
	while x_score < 5:
		user = x_won()
		if user == 3:
			x_score += 1

		print(x_score)
	print(x_score)
	break
