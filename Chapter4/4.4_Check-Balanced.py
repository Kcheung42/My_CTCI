# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    4.4_Check-Balanced.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/09/03 19:45:40 by kcheung           #+#    #+#              #
#    Updated: 2017/09/19 23:06:48 by kcheung          ###   ########.fr        #
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

def height(root):
	if root is None:
		return -1
	return max(height(root.left), height(root.right)) + 1
	
def isBalanced(root):
	if root is None:
		return True
	lh = height(root.left)
	rh = height(root.right)
	if abs(lh - rh) > 1:
		return False
	else:
		return isBalanced(root.left) and isBalanced(root.right)

array = [1,2,3,4,5,6,7]
bst = array_to_bst(array)
print isBalanced(bst)
