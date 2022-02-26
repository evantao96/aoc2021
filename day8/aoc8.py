import numpy as np 

signals = []
with open('input8.txt', 'r') as f:
	for l in f:
		signals += [[l.split('|')[0].strip().split(), l.split('|')[1].strip().split()]]
#print(signals)

#digitCount = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
#for n in signals: 
#	for s in n[1]:
#		if (len(s) == 2): 
#			digitCount['1'] += 1
# 		if (len(s) == 4): 
# 			digitCount['4'] += 1
# 		if (len(s) == 3):
# 			digitCount['7'] += 1
# 		if (len(s) == 7):
# 			digitCount['8'] += 1

# print(digitCount['1'] + digitCount['4'] + digitCount['7'] + digitCount['8']) 

sumOutputs = 0
for n in signals:
	digits = {}
	for s in n[0]: 
		if (len(s) == 2): 
			digits['1'] = frozenset(s)
			digits[frozenset(s)] = '1'
		if (len(s) == 4): 
			digits['4'] = frozenset(s)
			digits[frozenset(s)] = '4'
		if (len(s) == 3):
			digits['7'] = frozenset(s)
			digits[frozenset(s)] = '7'
		if (len(s) == 7):
			digits['8'] = frozenset(s)
			digits[frozenset(s)] = '8'

	segment_cf = digits['1']
	segment_bd = digits['4'].difference(digits['1'])
	segment_eg = digits['8'].difference(digits['4'].union(digits['7'].difference(digits['1'])))

	for s in n[0]: 
		if (len(s) == 6):
			if (len(set(s).intersection(segment_bd)) == 1):
				digits['0'] = frozenset(s)
				digits[frozenset(s)] = '0'
			if (len(set(s).intersection(segment_cf)) == 1):
				digits['6'] = frozenset(s)
				digits[frozenset(s)] = '6'
			if (len(set(s).intersection(segment_eg)) == 1):
				digits['9'] = frozenset(s)
				digits[frozenset(s)] = '9'
		if (len(s) == 5):
			if (segment_eg.issubset(set(s))):
				digits['2'] = frozenset(s)
				digits[frozenset(s)] = '2'
			if (segment_cf.issubset(set(s))):
				digits['3'] = frozenset(s)
				digits[frozenset(s)] = '3'
			if (segment_bd.issubset(set(s))):
				digits['5'] = frozenset(s)
				digits[frozenset(s)] = '5'

	num = ""
	for s in n[1]:
		num += digits[frozenset(s)]
	sumOutputs += int(num)

print(sumOutputs)
