import numpy as np 

with open('input5.txt', 'r') as f:
	contents = [l.strip().split() for l in f.readlines()]

start = []
end = []
for elem in contents: 
	start += [[int(k) for k in (elem[0].split(','))]]
	end += [[int(k) for k in (elem[2].split(','))]]

maxElem = max(np.max(start), np.max(end))

grid = np.zeros((maxElem+1, maxElem+1))

for i in range(len(start)): 
	startX = start[i][0]
	startY = start[i][1]
	endX = end[i][0]
	endY = end[i][1]

	yVector = 1 if (startY < endY) else -1
	xVector = 1 if (startX < endX) else -1

	i = startY
	j = startX

	if (startX == endX): # vertical line
		while(i != endY + yVector):
			grid[i, startX] += 1
			i += yVector

	elif (startY == endY): # horizontal line
		while(j != endX + xVector):
			grid[startY, j] += 1
			j += xVector

	else: # diagonal line
		while(i != endY + yVector):
			grid[i, j] += 1
			i += yVector
			j += xVector

print(np.count_nonzero(grid > 1))
