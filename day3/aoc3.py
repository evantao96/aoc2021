with open('input3.txt', 'r') as f:
	contents = [l.strip() for l in f.readlines()]

#part 1
gamma = ""
epsilon = ""

for i in range(len(contents[0])):
	gamma += '1' if sum([int(b[i]) for b in contents]) >= len(contents)/2 else '0'
	epsilon += '0' if sum([int(b[i]) for b in contents]) >= len(contents)/2 else '1'

print(int(gamma, 2) * int(epsilon, 2))

#part 2
oxygen = co2 = contents

i = 0
while(len(oxygen) > 1):
	mcb = '1' if sum([int(b[i]) for b in oxygen]) >= len(oxygen)/2 else '0'
	oxygen = [b for b in oxygen if b[i] == mcb]
	i = i + 1

i = 0
while(len(co2) > 1):
	lcb = '0' if sum([int(b[i]) for b in co2]) >= len(co2)/2 else '1'
	co2 = [b for b in co2 if b[i] == lcb]
	i = i + 1

print(int(oxygen[0], 2) * int(co2[0], 2))