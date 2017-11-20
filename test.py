# **************************************************************************** #
#                                                                              #
#                                                     .-. .-')                 #
#    test.py                                            :+:      :+:    :+:    #
#                                                     ,--. ,--.   .-----.      #
#    By: kcheung <kcheung@42.fr>                      |  .'   /  '  .--./      #
#                                                     |      /,  |  |('-.      #
#    Created: 2017/10/26 17:45:15 by kcheung          |     ' _)/_) |OO  )     #
#    Updated: 2017/10/31 21:36:54 by kcheung          ###   ########.fr        #
#                                                     |  |\   \(_'  '--'\      #
# **************************************************************************** #

class Vertex:
	def __init__(self, n):
		self.name = n
		self.neighbors = list()
		self.color = 'white'
	
	def add_neighbors(self, v):
		if v not in self.neighbors:
			self.neighbors.append(v)
			self.neighbors.sort()

class Graph:
	vertices = {}
