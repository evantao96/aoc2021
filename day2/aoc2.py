with open('input2.txt', 'r') as f:
	contents = [l.strip() for l in f.readlines()]

forward = 0
depth = 0
aim = 0

#for i in contents: 
#	if (i[0] == 'f'):
#		forward += int(i[-1])
#	if (i[0] == 'd'):
#		depth += int(i[-1])
#	if (i[0] == 'u'):
#		depth -= int(i[-1])

for i in contents: 
	if (i[0] == 'f'):
		forward += int(i[-1])
		depth += aim * int(i[-1])
	if (i[0] == 'd'):
		aim += int(i[-1])
	if (i[0] == 'u'):
		aim -= int(i[-1])

print(forward * depth)
