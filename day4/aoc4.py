import numpy as np

with open('input4.txt', 'r') as f:
	nums = [int(l.strip()) for l in f.readline().split(',')]
	contents = [int(k)for l in f.readlines() for k in l.strip().split() if l.strip()]

rows = []
for i in range(0, len(contents), 5): 
	rows += [[contents[i], 	
			contents[i+1],
			contents[i+2],
			contents[i+3],
			contents[i+4]]]

columns = []
for i in range(0, len(rows), 5):
	columns += np.array([rows[i], 
						rows[i+1], 
						rows[i+2], 
						rows[i+3], 
						rows[i+4]]).T.tolist()

score = 0
win = False

for num in nums:
	for i in range(len(rows)):
		rows[i] = [elem if elem != num else np.nan for elem in rows[i]]
		columns[i] = [elem if elem != num else np.nan for elem in columns[i]]
		if (all(np.isnan(rows[i])) or all(np.isnan(columns[i]))):
			score = int(np.nansum(np.nansum(np.array([rows[i-(i%5)], 
									rows[i-(i%5)+1],
									rows[i-(i%5)+2],
									rows[i-(i%5)+3],
									rows[i-(i%5)+4]])))) * num
			win = True
			break
	if (win):
		print(score)
		break

gameOver = False

for num in nums:
	for i in range(len(rows)):
		rows[i] = [elem if elem != num else np.nan for elem in rows[i]]
		columns[i] = [elem if elem != num else np.nan for elem in columns[i]]
		if (all(np.isnan(rows[i])) or all(np.isnan(columns[i]))):
			score = int(np.nansum(np.nansum(np.array([rows[i-(i%5)], 
									rows[i-(i%5)+1],
									rows[i-(i%5)+2],
									rows[i-(i%5)+3],
									rows[i-(i%5)+4]])))) * num
			rows[i-(i%5)] = []
			rows[i-(i%5)+1] = []
			rows[i-(i%5)+2] = []
			rows[i-(i%5)+3] = []
			rows[i-(i%5)+4] = []
									
			columns[i-(i%5)] = []
			columns[i-(i%5)+1] = []
			columns[i-(i%5)+2] = []
			columns[i-(i%5)+3] = []
			columns[i-(i%5)+4] = []

		if (not any(rows)):
			gameOver = True
			break
	if (gameOver):
		print(score)
		break