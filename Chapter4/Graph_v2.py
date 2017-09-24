# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Graph_v2.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/09/01 16:30:16 by kcheung           #+#    #+#              #
#    Updated: 2017/09/13 15:04:48 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Vertex:
	def __init__(self, n):
		self.name = n
		self.neighbors = list()
	
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

	def print_graph(self):
		for key in sorted(self.vertices.keys()):
			print(str(key) + str(self.vertices[key].neighbors))

