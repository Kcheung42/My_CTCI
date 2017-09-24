# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    3.1_Three-in-One.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/08/30 15:47:28 by kcheung           #+#    #+#              #
#    Updated: 2017/09/06 17:41:30 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Describe how you could use a single array to implement three stacks

class multiStack:
	def __init__(self, stacksize):
		self.stacknum = 3
		self.array = [0] * self.stacknum * stacksize
		self.sizes = [0] * self.stacknum
		self.capacity = stacksize
	
	def isEmpty(self, stacknum):
		return self.sizes[stacknum] == 0

	def isFull(self, stacknum):
		return self.sizes[stacknum] == self.capacity

	def peek(self, stacknum):
		if isEmpty(stacknum):
			raise Exception('stack is empty')
		return indexOfTop(stacknum)

	def push(self, stacknum, data):
		if self.isFull(stacknum):
			raise Exception('stack is full')
		self.sizes[stacknum] += 1
		self.array[self.indexOfTop(stacknum)] = data

	def pop(self, stacknum):
		if self.isEmpty(stacknum):
			raise Exception("stack is empty")
		self.sizes[stacknum] -= 1
		# self.array[indexOfTop(stacknum)] = 0

	def indexOfTop(self, stacknum):
		offset = stacknum * self.capacity
		return (offset + self.sizes[stacknum] - 1)

	def printstack(self, stacknum):
		if self.isEmpty(stacknum):
			return "stack is Empty"
		else:
			offset = stacknum * self.capacity
			print (self.array[offset : self.indexOfTop(stacknum)+1])

newstack = multiStack(10)
newstack.push(0,3)
newstack.push(0,3)
newstack.push(0,3)
newstack.push(0,3)
newstack.pop(0)
newstack.pop(0)
newstack.push(0,4)

newstack.printstack(0)
