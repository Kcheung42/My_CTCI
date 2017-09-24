# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    stacks.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/08/30 16:23:47 by kcheung           #+#    #+#              #
#    Updated: 2017/08/30 17:02:51 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Basic Stack implementation using linked lists

class StackNode:
	def __init__(self, value=None, nextNode=None):
		self.value = value
		self.next = nextNode

class Stack:
	def __init__(self, values=None):
		self.top = None
		if values is not None:
			self.pushMulti(values)

	def isEmpty(self):
		return self.top == None

	def peek(self):
		if self.isEmpty():
			return float("-inf")
		return self.top.value

	def push(self,value):
		self.top = StackNode(value, self.top)
	
	def pushMulti(self, values=None):
		if values is not None:
			for v in values:
				self.push(v)
	
	def pop(self):
		if self.isEmpty():
			return float("-inf")
		temp = self.top
		self.top = self.top.next
		popped = temp.value
		return popped

	def printstack(self):
		if self.isEmpty():
			return
		cur = self.top
		while(cur):
			print(cur.value)
			cur = cur.next
		print ("---Bottom---")

# stack = Stacks([1,2,3,4,5,6])
# stack.pop()
# stack.printstack()
# print stack.peek()
