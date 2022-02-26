import numpy as np 

with open('input6.txt', 'r') as f:
	contents = [l.strip() for l in f.readline().split(',')]

time = 256
nums = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0}
for n in contents:
	nums[n] += 1
print(nums)

while (time > 0):
	time -= 1
	numZeros = nums['0']
	nums['0'] = nums['1']
	nums['1'] = nums['2']
	nums['2'] = nums['3']
	nums['3'] = nums['4']
	nums['4'] = nums['5']
	nums['5'] = nums['6']
	nums['6'] = numZeros + nums['7']
	nums['7'] = nums['8']
	nums['8'] = numZeros

print(sum(nums.values()))

