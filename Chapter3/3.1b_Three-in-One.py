# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    3.1b_Three-in-One.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/08/30 15:50:07 by kcheung           #+#    #+#              #
#    Updated: 2017/11/27 21:13:54 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Describe how you could use a single array to implement three stacks

class multiStack:
	def __init__(self, numstacks, arraysize):
		self.peeks = [-1 for _ in range(numstacks)]
		self.stackVal = [0 for _ in range(arraysize)]
		self.index = list(range(1,arraysize))
		self.index.append(-1)
		self.availIndex = 0

	def isEmpty(self, stacknum):
		return self.peeks[stacknum] == -1

	def isFull(self, stacknum):
		return self.availIndex == -1

	def push(self, stacknum, val):
		if stacknum < 0 or stacknum >= len(self.peeks):
			raise Exception("Invalid Stack number")
		if self.isFull(stacknum):
			return "Stack is Full"
		self.stackVal[self.availIndex] = val
		prePeek = self.peeks[stacknum]
		self.peeks[stacknum] = self.availIndex
		nextIndex = self.index[self.availIndex]
		self.index[self.availIndex] = prePeek
		self.availIndex = nextIndex
	
	def pop(self, stacknum):
		if stacknum < 0 or stacknum >= len(self.peeks):
			raise Exception("Invalid Stack number")
		if self.isEmpty(stacknum):
			return "Stack is Empty"
		val = self.stackVal[self.peeks[stacknum]]
		prePeek = self.peeks[stacknum]
		self.peeks[stacknum] = self.index[prePeek]
		self.index[prePeek] = self.availIndex
		self.availIndex = prePeek
		return val
	
	def printStack(self, stacknum):
		while(not self.isEmpty(stacknum)):
			print self.pop(stacknum)

plates = multiStack(3,6)
plates.push(0,5)
plates.push(0,6)
plates.push(1,7)
plates.pop(0)
plates.push(2,8)
plates.push(0,9)

print plates.peeks
print plates.stackVal
print plates.index

plates.printStack(0)
