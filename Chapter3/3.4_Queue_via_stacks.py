# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    3.4_Queue_via_stacks.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/08/30 13:38:21 by kcheung           #+#    #+#              #
#    Updated: 2017/08/30 14:59:22 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Queue via Stacks: Implement a MyQueue class which implements a queueusing
# two stacks.

from stack import Stack

class Queue:
	def __init__(self):
		self.newstack = Stack()
		self.oldstack = Stack()

	def peek(self):
		self.transfer()
		return self.oldstack.peek()

	def isEmpty(self):
		self.transfer()
		return self.oldstack.isEmpty()

	def enqueue(self, val):
		self.newstack.push(val) 

	def dequeue(self):
		self.transfer()
		return self.oldstack.pop()

	def transfer(self):
		if self.oldstack.isEmpty():
			while not self.newstack.isEmpty():
				self.oldstack.push(self.newstack.pop())

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print "peek is:%d" % q.peek()
print q.dequeue()
print q.dequeue()
print q.dequeue()
print q.dequeue()
q.enqueue(6)
q.enqueue(7)
q.enqueue(8)
q.enqueue(9)
print q.dequeue()
print q.dequeue()
print q.dequeue()
print q.dequeue()
print q.dequeue()

print q.isEmpty()
