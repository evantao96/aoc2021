import math 

with open('input17.txt', 'r') as f: 
	contents = f.readlines()[0].strip().split()

startX = int(contents[2].split('=')[1].split('..')[0])
endX = int(contents[2].split('=')[1].split('..')[1][:-1])
startY = int(contents[3].split('=')[1].split('..')[0])
endY = int(contents[3].split('=')[1].split('..')[1])

target = [(i, j) for i in range(startX, endX+1) for j in range(startY, endY+1)]

overallMax = []
initialV = set()

for i in range(0, 70):
	for j in range(-230, 300):
		
		vX = i 
		vY = j

		x = 0
		y = 0

		tentativeMax = 0

		while (y > startY):

			x += vX
			y += vY

			if (y > tentativeMax):
				tentativeMax = y

			if (x, y) in target:
				overallMax.append(tentativeMax)
				initialV.add((i, j))
				print("Found max: " + str(tentativeMax))
				print("Found initial velocity: " + str(i) + " " + str(j))

			if (vX > 0):
				vX -= 1
			elif (vX < 0): 
				vX += 1
			vY -= 1

print("Overall max: " + str(max(overallMax)))
#print(initialV)
print("Number of distinct initial velocities: " + str(len(initialV)))




