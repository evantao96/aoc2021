import math

with open('input9.txt', 'r') as f:
	rowLength = len(f.readline().strip())
	f.seek(0)
	contents = [math.inf] * rowLength
	for l in f.readlines():
		for k in l.strip():
			contents += [int(k)]
		contents += [math.inf]
	contents += [math.inf] * rowLength

riskLevel = 0
sinkPoints = []

for i in range(rowLength, len(contents)-rowLength):
	if(contents[i] < contents[i-1] and
		contents[i] < contents[i+1] and
		contents[i] < contents[i+rowLength+1] and
		contents[i] < contents[i-rowLength-1]):
		#riskLevel += contents[i] + 1
		sinkPoints += [i]
#print(riskLevel)

def countLocations(i):
	if (contents[i] == 9 or contents[i] == math.inf):
		return 0
	else: 
		temp = contents[i]
		contents[i] = math.inf
		sumLocations = 1
		if(temp < contents[i-1]):
			sumLocations += countLocations(i-1)
		if(temp < contents[i+1]):
			sumLocations += countLocations(i+1)
		if(temp < contents[i+rowLength+1]):
			sumLocations += countLocations(i+rowLength+1)
		if(temp < contents[i-rowLength-1]):
			sumLocations += countLocations(i-rowLength-1)
	return sumLocations

basins = [countLocations(i) for i in sinkPoints]
basins.sort()
print(basins[-1]*basins[-2]*basins[-3])




