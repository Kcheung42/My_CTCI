# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    4.3_List-of-Depth.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/09/03 15:32:31 by kcheung           #+#    #+#              #
#    Updated: 2017/10/05 10:45:29 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Given a binary tree, design an algorithm which creates a linked list of all
# the nodes at each depth

class BinaryTree:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
	def __str__(self):
		return "( " + str(self.val) + " ( " + str(self.left) + " | " + str(self.right) + "))" 

class LinkedList:
	def __init__(self, value=None , nextNode=None):
		self.val = value
		self.next = nextNode

	def __str__(self):
		return "->" + str(self.val) + str(self.next) + " )"

def bst_to_linked_list(btree, depth=1, returnlist=[]):
	# print "printing depth:%d returnlist len:%d" %(depth, len(returnlist))
	# count = 0
	# for ll in returnlist:
	# 	count += 1
	# 	print str(count)  + " : head" + str(ll)
	if len(returnlist) >= depth:
		returnlist[depth-1] = LinkedList(btree.val, returnlist[depth-1])
	else:
		returnlist.append(LinkedList(btree.val))
	if btree.left is not None:
		returnlist =  bst_to_linked_list(btree.left, depth + 1, returnlist)
	if btree.right is not None:
		returnlist =  bst_to_linked_list(btree.right, depth + 1, returnlist)
	return returnlist

def makeBalanced(array, start, end):
	if start > end:
		return None
	mid = (start + end) / 2
	root = BinaryTree(array[mid])
	root.left = makeBalanced(array, start, mid-1)
	root.right = makeBalanced(array, mid + 1, end)
	return root

array = [1,2,3,4,5,6,7]
bst = makeBalanced(array, 0, 6)
list = bst_to_linked_list(bst)

count = 0
for ll in list:
	count += 1
	print str(count)  + " : head" + str(ll)

