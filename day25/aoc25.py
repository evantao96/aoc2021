cucumbers = {}

with open('input25.txt', 'r') as f: 
	i = 0
	for l in f.readlines():
		j = 0
		for c in l.strip():
			cucumbers[i, j] = c 
			j += 1
		i += 1

rows = i
cols = j

new_cucumbers = cucumbers.copy()
steps = 0

while (True):
	has_moved = False
	for coords, chars in cucumbers.items():
		if chars == '>':
			if coords[1] < cols - 1:
				new_coords = (coords[0], coords[1]+1)
			else: 
				new_coords = (coords[0], 0)
			if cucumbers[new_coords] == '.':
				has_moved = True
				new_cucumbers[new_coords] = '>'
				new_cucumbers[coords] = '.'

	cucumbers = new_cucumbers.copy()

	for coords, chars in cucumbers.items():
		if chars == 'v':
			if coords[0] < rows - 1:
				new_coords = (coords[0]+1, coords[1])
			else: 
				new_coords = (0, coords[1])
			if  cucumbers[new_coords] == '.':
				has_moved = True
				new_cucumbers[new_coords] = 'v'
				new_cucumbers[coords] = '.'

	cucumbers = new_cucumbers.copy()
	steps += 1
	print(steps)
	if not has_moved:
		break

