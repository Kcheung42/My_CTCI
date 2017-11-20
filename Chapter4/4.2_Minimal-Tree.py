# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    4.2_Minimal-Tree.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/09/03 14:58:16 by kcheung           #+#    #+#              #
#    Updated: 2017/10/05 10:29:37 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Given a sorted (increasing order) array with unique integer elements,
# write an algorithm to create a binary search tree with minimal height

class BinaryTree:
	def __init__(self, value):
		self.left = None
		self.right = None
		self.val = value

def createBST(array, start, end):
	if start < end:
		mid = (start + end) / 2
		root = BinaryTree(array[mid])
		root.left = createBST(array, start, mid - 1)
		root.right = createBST(array, mid + 1, end)
		return root

def array_to_BST(array):
	createBST(array, 0, len(array) - 1)

if __name__ == '__main__':
	array = [1,2,3,4,5,6,7]
	array_to_BST(array)

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def createBST(array, start, end):
    if start < end:
        mid =(start + end) / 2
        root = BinaryTree(array[mid])
        root.right = createBST(array, start, mid-1)
        root.left = createBST(array, mid+1, end)
