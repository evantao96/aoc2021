# def find_winner(pos):
# 	num_rolls = 0
# 	roll = 1
# 	scores = {1: 0, 2: 0}
# 	while (True):
# 		player = num_rolls % 2 + 1
# 		pos[player] += roll + (roll + 1) + (roll + 2)
# 		pos[player] = (pos[player] - 1) % 10 + 1
# 		scores[curr] += pos[player]

# 		roll += 3
# 		num_rolls += 3

# 		if (scores[curr] >= 1000):
# 			return (scores, num_rolls)

# print(find_winner(init_pos))

rolls = {3:1, 4:3, 5:6, 6:7, 7:6, 8:3, 9:1}
cache = {}

def find_wins(pos, player, scores):
	global cache

	if (pos, player, scores) in cache: 
		return cache[(pos, player, scores)]

	if scores[1] >= 21:
		return 1
	elif scores[0] >= 21: 
		return 0

	wins = 0
	for r, n in rolls.items(): 
		next_pos = list(pos)
		next_scores = list(scores)

		next_pos[player] = (next_pos[player] + r - 1) % 10 + 1
		next_scores[player] += next_pos[player]

		wins += find_wins(tuple(next_pos), int(not player), tuple(next_scores)) * n

	cache[(pos, player, scores)] = wins
	return wins

init_pos = (10, 4)
init_player = 0
init_scores = (0, 0)
print(find_wins(init_pos, init_player, init_scores))
