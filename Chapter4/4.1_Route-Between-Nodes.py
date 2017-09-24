# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    4.1_Route-Between-Nodes.py                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/08/30 18:56:31 by kcheung           #+#    #+#              #
#    Updated: 2017/09/03 22:17:37 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Given a directed graph, design an algorithm to find out whether there is a
# route between two nodes

# No import libraries

class Vertex:
	def __init__(self, n):
		self.name = n
		self.neighbors = list()
		self.color = 'white'
	
	def add_neighbor(self, v):
		if v not in self.neighbors:
			self.neighbors.append(v)
			self.neighbors.sort()

class Graph:
	vertices = {}
	def add_vertex(self, vertex):
		if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
			self.vertices[vertex.name] = vertex
			return True
		else:
			return False

	def add_edge(self, u, v):
		if u in self.vertices and v in self.vertices:
			for key, value in self.vertices.items():
				if key == u:
					value.add_neighbor(v)
				if key == v:
					value.add_neighbor(u)
		else:
			self.add_vertex(Vertex(u))
			self.add_vertex(Vertex(v))
			self.add_edge(u,v)
			

	# DFS
	def isRoute(self, start, end):
		if start == end:
			return True
		start.color = 'grey'
		for next in start.neighbors:
			if self.vertices[next].color == 'white':
				return self.isRoute(self.vertices[next],end)
		start.color = 'black'
		return False

	# BFS
	def isRoute2(self, start, end):
		if start == end:
			return True
		start.color = 'grey'
		q = []
		q.append(start)
		while q:
			start = q.pop(0)
			if start == end:
				return True
			for next in start.neighbors:
				if self.vertices[next].color == 'white':
					q.append(self.vertices[next])
			start.color = 'black'
		return False


	def print_graph(self):
		for key in sorted(self.vertices.keys()):
			print(str(key) + str(self.vertices[key].neighbors))

g = Graph()
edges = ['AB', 'AC', 'ED', 'BD', 'BE','DE', 'YZ']

for i in range(ord('A'),ord('Z'),2):
	g.add_vertex(Vertex(chr(i)))
for edge in edges:
	g.add_edge(edge[:1], edge[1:])

# g.print_graph()
# print g.isRoute(g.vertices['A'], g.vertices['B'])
print g.isRoute2(g.vertices['C'], g.vertices['B'])

