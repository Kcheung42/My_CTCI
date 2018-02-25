# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Graph_v2.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/09/01 16:30:16 by kcheung           #+#    #+#              #
#    Updated: 2018/02/19 23:25:42 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

'''
 This is an undirected weighted graph class Implementation
'''

from heapq import *

class Vertex:
	def __init__(self, n):
		self.name = n
		self.neighbors = list()
	
	def add_neighbor(self, v):
		if v not in self.neighbors:
			self.neighbors.append(v)

class Graph:
	vertices = {}
	def add_vertex(self, vertex):
		if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
			self.vertices[vertex.name] = vertex
			return True
		else:
			return False

	def add_edge(self, u, v, c):
		if u in self.vertices and v in self.vertices:
			for key, val in self.vertices.items():
				if key == u:
					val.add_neighbor((c,self.vertices[v]))
				if key == v:
					val.add_neighbor((c,self.vertices[u]))
		else:
			self.add_vertex(Vertex(u))
			self.add_vertex(Vertex(v))
			self.add_edge(u,v,c)

	def dijkstra(self, f, t):
		if f not in self.vertices or t not in self.vertices:
			return False
		q = [(0, f, ())]
		seen = set()
		while q:
			(cost, v1, path) = heappop(q)
			if v1 not in seen:
				seen.add(v1)
				path = (v1, path)
			if v1 == t: return (cost, path)
			for c, val in self.vertices[v1].neighbors:
				v2 = val.name
				if v2 not in seen:
					heappush(q, (cost+c, v2 , path))
		return(False)

	def print_graph(self):
		for key in sorted(self.vertices.keys()):
			print(str(key) + str(self.vertices[key].neighbors))


if __name__ == "__main__":
	g = Graph()
	g.add_edge('S', 'B', 2)
	g.add_edge('S', 'A', 7)
	g.add_edge('S', 'C', 3)
	g.add_edge('A', 'B', 3)
	g.add_edge('A', 'D', 4)
	g.add_edge('D', 'B', 4)
	g.add_edge('D', 'F', 5)
	g.add_edge('B', 'H', 1)
	g.add_edge('H', 'F', 3)
	g.add_edge('H', 'G', 2)
	g.add_edge('G', 'E', 2)
	g.add_edge('C', 'L', 2)
	g.add_edge('L', 'I', 4)
	g.add_edge('L', 'J', 4)
	g.add_edge('I', 'J', 6)
	g.add_edge('I', 'K', 4)
	g.add_edge('J', 'K', 4)
	g.add_edge('K', 'E', 5)

	print("=== Dijkstra ===")
	print("S -> E:")
	print(g.dijkstra('S', 'E'))
