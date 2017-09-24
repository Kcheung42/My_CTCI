# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    4.4b_Check-Balance.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/09/03 20:41:57 by kcheung           #+#    #+#              #
#    Updated: 2017/09/19 23:07:17 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class BinaryTree:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

	def __str__(self):
		return "( " + str(self.val) + " ( " + str(self.left) + " | " + str(self.right) + "))" 

def create_bst(array, start, end):
	if start > end:
		return None
	mid = (start + end) / 2
	root = BinaryTree(array[mid])
	root.left = create_bst(array, start, mid-1)
	root.right = create_bst(array, mid + 1, end)
	return root

def array_to_bst(array):
	return create_bst(array, 0, len(array)-1)

# Question: implement a function to check if a binary tree is balanced. For
# the purposes of this question, a balanced tree is defined to be a tree such
# that the heights of the two subtrees of any node never differ by more than one

def checkHeight(root):
	if root is None:
		return -1

	leftheight = checkHeight(root.left)
	if leftheight == float(-inf):
		return float(-inf)
	rightheight = checkHeight(root.right)
	if rightheight == float(-inf):
		return float(-inf)

	diff = abs(leftheight - rightheight)
	if diff > 1:
		return float(-inf)
	else:
		return max(leftheight, rightheight) + 1

def isBalanced(root):
	return checkHeight(root) is not (-inf)


# Time: O(n)
# Space: O(h) where h is height of tree
