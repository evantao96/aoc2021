import numpy as np 
from numpy.lib.stride_tricks import sliding_window_view

with open('input20.txt', 'r') as f:
	algorithm = f.readline().strip()
	input_image = [list(l.strip()) for l in f.readlines() if l.strip()]

iterations = 50
n = iterations * 2

input_image = np.pad(np.array(input_image), n, constant_values='.')
output_image = np.full(input_image.shape, '.')

pixel_dict = {'.':'0', '#':'1'}

for i in range(iterations):
	count = 0
	square_views = sliding_window_view(input_image, (3,3))
	for j in range(len(square_views)):
		for k in range(len(square_views[0])):
			output_string = [p for row in square_views[j][k] for p in row]
			output_binary = ''.join([pixel_dict[p] for p in output_string])
			output_pixel = algorithm[int(output_binary, 2)]
			output_image[j][k] = output_pixel
			if (output_pixel == '#'):
				count += 1
	output_image = output_image[:-2, :-2]
	input_image = output_image.copy()

	print("Final count: " + str(count))