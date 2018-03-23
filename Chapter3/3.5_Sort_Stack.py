# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    3.5_Sort_Stack.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/08/30 14:59:50 by kcheung           #+#    #+#              #
#    Updated: 2017/08/30 18:55:30 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Write a program to sort a stack such that the smallest items are on the top.
# You can use an additional temporary stack, but you may not copy the elements
# into any other data structure (such as an array).
# The stack supports the following operations: push, pop, peek and isEmpty

# Time O(N^2)
# Space O(N)

from stacks import Stack

def sort(stack):
	tempstack = Stack()
	while not stack.isEmpty():
		temp = stack.pop()
		while not tempstack.isEmpty() and tempstack.peek() > temp:
			stack.push(tempstack.pop())
		tempstack.push(temp)
	while not tempstack.isEmpty():
		stack.push(tempstack.pop())
	return stack

if __name__ == "__main__":
	stack = Stack([1,2,3,4,5,6])
	stack.printstack()
	stack = sort(stack)
	stack.printstack()

