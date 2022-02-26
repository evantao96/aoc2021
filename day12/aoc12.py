import math 

with open('input12.txt', 'r') as f: 
	graph = {}
	for v1,v2 in [l.strip().split('-') for l in f.readlines()]:
		if v1 in graph:
			graph[v1].append(v2)
		else:
			graph[v1] = [v2]

		if v2 in graph:
			graph[v2].append(v1)
		else:
			graph[v2] = [v1]
#print(graph)

# def countPaths(v1, visited):
# 	if(v1 == 'end'):
# 		return 1
# 	else:
# 		sumPaths = 0
# 		for v2 in graph[v1]:
# 			if (v2 not in visited or v2.isupper()):
# 				sumPaths += countPaths(v2, visited+[v2])
# 		return sumPaths

# print(countPaths('start', ['start']))

def countPaths2(v1, visited, doubled):
	if(v1 == 'end'):
		print(visited)
		return 1
	else:
		sumPaths = 0
		for v2 in graph[v1]:
			if (v2 not in visited or v2.isupper()):
				sumPaths += countPaths2(v2, visited+[v2], doubled)
			elif (v2 != 'start' and not doubled):
				sumPaths += countPaths2(v2, visited+[v2], True)
		return sumPaths

print(countPaths2('start', ['start'], False))