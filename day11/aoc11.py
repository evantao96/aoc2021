import math 

N = 12
contents = []
with open('input11.txt', 'r') as f:
	for l in f.readlines():
		contents += [-math.inf] + [int(k) for k in l.strip()] + [-math.inf]
	contents = [-math.inf] * N + contents + [-math.inf] * N

start = N+1
end = len(contents)-N-1

flash_list = []
#total = 0
step = 0

#for step in range(100):
while (True): # break when there are (N-2)*(N-2) zeros
	contents = [n+1 for n in contents]
	step += 1

	while (True): # break when num_flashes remains 0
		num_flashes = 0
		for i in range(start, end):
			if(contents[i] > 9 and i not in flash_list):
				num_flashes += 1
				flash_list.append(i)
				contents[i-N-1] += 1
				contents[i-N] += 1
				contents[i-N+1] += 1
				contents[i-1] += 1
				contents[i+1] += 1
				contents[i+N-1] += 1
				contents[i+N] += 1
				contents[i+N+1] += 1

		#total += num_flashes

		if (num_flashes == 0):
			break

	contents = [0 if ind in flash_list else num for ind, num in enumerate(contents)]
	flash_list.clear()

	if (contents.count(0) == (N-2)*(N-2)):
		break

#print(total)
print(step)