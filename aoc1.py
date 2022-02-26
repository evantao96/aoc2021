with open('input.txt', 'r') as f:
	contents = [int(l.strip()) for l in f.readlines()]

depth = 0
#for i in range(1,len(contents)): 
	#if (contents[i] > contents[i-1]):
	#	depth += 1

for i in range(1,len(contents)-2): 
	window = contents[i] + contents[i+1] + contents[i+2]
	prev_window = contents[i-1] + contents[i] + contents[i+1]
	if (window > prev_window):
		depth += 1

print(depth)