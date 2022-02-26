with open('input10.txt', 'r') as f: 
	contents = [l.strip() for l in f.readlines()]

openChars = ['(', '[', '{', '<']
closeChars = [')', ']', '}', '>']
dictChars = dict(zip(openChars, closeChars))
count = dict(zip(closeChars, [0, 0, 0, 0]))

corrupted = set()
for line in contents:
	stack = []
	for curr in line:
		if (curr in openChars):  
			stack.append(curr)
		elif (curr in closeChars):
			expected = dictChars[stack.pop()]
			if (expected != curr):
				#print("Expected " + expected + ", but found " + curr + " instead.")
				count[curr] += 1
				corrupted.add(line)

# print(count[')']*3 + count[']']*57 + count['}']*1197 + count['>']*25137)

incomplete = list(set(contents) - corrupted) 
multiplier = dict(zip(openChars, [1, 2, 3, 4]))
scores = []

for line in incomplete:
	stack = []
	score = 0
	for curr in line:
 		if (curr in openChars):  
 			stack.append(curr)
 		elif (curr in closeChars):
 			stack.pop()

	while (stack):
		score = score * 5 + multiplier[stack.pop()]
	scores += [score]

scores.sort()
mid = int((len(scores)-1)/2)
print(scores[mid])
