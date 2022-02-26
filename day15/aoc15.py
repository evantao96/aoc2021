import math
import heapq

graph = []
with open('input15.txt', 'r') as f: 
	for l in f.readlines():
		graph += [[int(n) for n in l.strip()]]

temp = graph.copy()
for i in range(4):
	temp = [[elem+1 if elem < 9 else 1 for elem in row] for row in temp]
	graph.extend(temp)

graph = [[graph[j][i] for j in range(len(graph))] for i in range(len(graph[0]))]

temp = graph.copy()
for i in range(4):
	temp = [[elem+1 if elem < 9 else 1 for elem in row] for row in temp]
	graph.extend(temp)

graph = [[graph[j][i] for j in range(len(graph))] for i in range(len(graph[0]))]

n = len(graph)
m = len(graph[0])

unvisited = [(i, j) for i in range(n) for j in range(m)]

shortest_path = {node: math. inf for node in unvisited}
shortest_path[(0, 0)] = 0
min_heap = [(0, (0, 0))]

while unvisited: 
	current_min_dist, current_min_node = heapq.heappop(min_heap)

	if (current_min_node in unvisited):
		
		i = current_min_node[0]
		j = current_min_node[1]
		neighbors = []
		if i > 0: neighbors.append((i-1, j))
		if i + 1 < n: neighbors.append((i+1, j))
		if j > 0: neighbors.append((i, j-1))
		if j + 1 < n: neighbors.append((i, j+1))

		for neighbor in neighbors: 
			tentative_value = current_min_dist + graph[neighbor[0]][neighbor[1]]
			if (tentative_value < shortest_path[neighbor]):
				shortest_path[neighbor] = tentative_value
				heapq.heappush(min_heap, (tentative_value, neighbor))

		unvisited.remove(current_min_node)
		print("Nodes left to visit: " + str(len(unvisited)))

print(shortest_path)
print("Finished calculating shortest paths")
print(shortest_path[(n-1, m-1)])