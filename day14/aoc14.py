with open('input14.txt', 'r') as f: 
	poly = f.readline().strip()
	rules = dict([l.strip().split(' -> ') for l in f.readlines() if l.strip()])

pairs = [poly[i:i+2] for i in range(len(poly)-1)]
pairs = {i:pairs.count(i) for i in set(pairs)}
temp = pairs.copy()

# for i in range(10):
# 	for p in pairs:
# 		if p in rules: 
# 			pairs2.remove(p)
# 			pairs2.append(p[0]+rules[p])
# 			pairs2.append(rules[p]+p[1])
# 	pairs = pairs2.copy()

for i in range(40):
	for p in pairs:
		if p in rules: 
			n = pairs[p]
			temp[p] -= n #remove

			new_pair1 = p[0]+rules[p] #append new_pair1)
			if (new_pair1 in temp): 
				temp[new_pair1] += n
			else: 
				temp[new_pair1] = n

			new_pair2 = rules[p]+p[1] #append new_pair2
			if (new_pair2 in temp): 
				temp[new_pair2] += n
			else: 
				temp[new_pair2] = n

	pairs = temp.copy()

count = {}
for p in pairs: 
	n = pairs[p]
	letter = p[0]
	if letter in count: 
		#count[letter] += 1
		count[letter] += n
	else:  
		#count[letter] = 1
		count[letter] = n
count[poly[-1]] += 1

print(max(count.values()) - min(count.values()))