# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    4.6_Successor.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/09/05 19:53:27 by kcheung           #+#    #+#              #
#    Updated: 2017/10/05 11:49:02 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Successor: Write an algorithm to find the "next" node (i.e. in-order successor)
# of a given node in a binary search tree. You may assume that each node as a
# link to its parent.

class Node:
	def __init__(self, value=None, leftNode=None, rightNode=None, parent=None):
		self.val = value
		self.l = leftNode
		self.r = rightNode
		self.p = parent

def minVal(root):
	if root is None:
		return float(-inf)
	current = root
	while(cur is not None):
		if current is None:
			break
		current = current.l
	return current.val

# Insert a new node into BST
def insert(root, data):
	if root is None:
		return Node(data)
	else:
		if data <= root.val:
			temp = insert(root.l, data)
			root.l = temp
			temp.p = root
		else:
			temp = insert(root.r, data)
			root.r = insert(root.r, data)
			temp.p = root

def successor(node):
	if node.r is not None:
		return minVal(root.r)
	parent = node.p
	if parent is None:
		return "No Successor"
	while parent.p is not None:
		if parent != node.r:
			break
		node = parent
		parent = parent.p
	return parent

# Algorithm
# 1. If right subtree of node is not NULL, then succ lies in the right subtree.
# Do the following: Go to right subtree and return the node with minimum key
# value in right subtree.

# 2. if right subtree of node is NULL, then succ is on of the ancestors. Do the
# following: Travel up the Tree using the parent pointer until you see a node
# which is the left child of it's parent. That parent of such node is the succ
