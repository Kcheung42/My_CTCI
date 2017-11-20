from collections import defaultdict

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)
	
	def add_edge(self, u, v):
		self.graph[u].append(v)
	
	def DFS(self, start, end, visited=None):
		if visited is None:
			visited = set()
		if start == end:
			return True
		visited.add(start)
		for next in self.graph[start]:
			if next not in visited:
				if (self.DFS(next, end, visited)):
					return True
		return False

g = Graph()

edges = ['AB', 'AC', 'ED', 'BD', 'BE','DE', 'YZ']
for edge in edges:
	g.add_edge(edge[:1], edge[1:])

print g.DFS('A', 'Y')
print g.DFS('A', 'E')
