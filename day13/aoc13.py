import numpy as np
import matplotlib.pyplot as plt

dots = []
with open('input13.txt', 'r') as f: 
	while (True):
		l = f.readline()
		if (l == '\n'):
			break
		l = l.strip().split(',')
		dots += [[int(l[0]), int(l[1])]]

	folds = [l.split()[-1].split('=') for l in f.readlines()]

for fold in folds: 
	ind = 0 if fold[0] == 'x' else 1
	mid = int(fold[1])

	for d in dots: 
		if (d[ind] > mid): 
			d[ind] = 2*mid - d[ind]

dots = list(set([tuple(d) for d in dots]))

x, y = np.array(dots).T
plt.scatter(x, -1*y)
plt.show()