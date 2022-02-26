import numpy as np 

with open('input7.txt', 'r') as f:
	nums = [int(l.strip()) for l in f.readline().split(',')]

minNum = min(nums)
maxNum = max(nums)

dists = []
#for i in range(minNum, maxNum+1): 
#	sumDist = 0
#	for n in nums: 
#		sumDist += abs(n-i)
#	dists += [sumDist]

#print(min(dists))

steps = []
for i in range(0, maxNum-minNum+1):
	steps += [int(i*(i+1)/2)]

for i in range(minNum, maxNum+1): 
	sumDist = 0
	for n in nums: 
		sumDist += steps[abs(n-i)]
	dists += [sumDist]

print(min(dists))
