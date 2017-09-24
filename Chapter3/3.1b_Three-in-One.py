# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    3.1b_Three-in-One.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/08/30 15:50:07 by kcheung           #+#    #+#              #
#    Updated: 2017/09/19 22:34:47 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Describe how you could use a single array to implement three stacks

class multiStack:
	def __init__(self, numstacks, arraysize):
		self.topOfStacks = [-1 for _ in range(numstacks)]
		self.stackData = [0 for _ in range(arraysize)]
		self.next_index = list(range(1,arraysize))
		self.next_index.append(-1)
		self.nextAvailable = 0

	def isEmpty(self, stacknum):
		return self.topOfStacks[stacknum] == -1

	def isFull(self, stacknum):
		return self.nextAvailable == -1

	def push(self, stacknum, val):
		if stacknum < 0 or stacknum >= len(self.topOfStacks):
			raise Exception("Invalid Stack number")
		if self.isFull(stacknum):
			return "Stack is Full"
		self.stackData[self.nextAvailable] = val
		tempTop = self.topOfStacks[stacknum]
		self.topOfStacks[stacknum] = self.nextAvailable
		tempIdx = self.next_index[self.nextAvailable]
		self.next_index[self.nextAvailable] = tempTop
		self.nextAvailable = tempIdx
	
	def pop(self, stacknum):
		if stacknum < 0 or stacknum >= len(self.topOfStacks):
			raise Exception("Invalid Stack number")
		if self.isEmpty(stacknum):
			return "Stack is Empty"
		val = self.stackData[self.topOfStacks[stacknum]]
		tempTop = self.topOfStacks[stacknum]
		self.topOfStacks[stacknum] = self.next_index[tempTop]
		self.next_index[tempTop] = self.nextAvailable
		self.nextAvailable = tempTop
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

print plates.topOfStacks
print plates.stackData
print plates.next_index

plates.printStack(0)
