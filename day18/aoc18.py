with open('input18.txt', 'r') as f:
	nums = [[int(l.strip()[1]), int(l.strip()[3])] for l in f.readlines()]

def count_lists(l):
	count = 0
	if isinstance(l[0], list):
		count += 1
		count += count_lists(l[0])
	return count

for i in range(1, len(nums)):
	nums[i] = [nums[i-1], nums[i]]
