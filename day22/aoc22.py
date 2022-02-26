with open('input22.txt', 'r') as f: 
	contents = [l.strip() for l in f.readlines()]

cubes = {}
num_cubes = 0

for l in contents:
	status, coords = l.split(' ')
	x_coords, y_coords, z_coords = coords.split(',')

	x_start = int(x_coords.split('..')[0][2:])
	x_end = int(x_coords.split('..')[1])
	y_start = int(y_coords.split('..')[0][2:])
	y_end = int(y_coords.split('..')[1])
	z_start = int(z_coords.split('..')[0][2:])
	z_end = int(z_coords.split('..')[1])

	vol = (x_end-x_start+1)*(y_end-y_start+1)*(z_end-z_start+1)
	if (status == 'off'): vol *= -1
	num_cubes += vol
	
# 	if (x_start >= -50 and x_end <= 50 and 
# 		y_start >= -50 and y_end <= 50 and
# 		z_start >= -50 and z_end <= 50):
# 		for i in range(x_start, x_end+1): 
# 			for j in range(y_start, y_end+1):
# 				for k in range(z_start, z_end+1):
# 						cubes[(i, j, k)] = status	
# 						print((i, j, k))

# print(len([c for c in cubes if cubes[c] == 'on']))

print(num_cubes)