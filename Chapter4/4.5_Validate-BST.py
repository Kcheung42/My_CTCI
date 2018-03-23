# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    4.5_Validate-BST.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/09/03 20:56:55 by kcheung           #+#    #+#              #
#    Updated: 2017/10/03 14:17:38 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Validate BST: Implement a function to check if a binary tree is a binary
# search tree

# Use inorder traversal to see if out put is in order

# given structure:

# class BST:
#     def __init__(self, data, left=None, right=None):
#         self.data = data
#         self.l = left
#         self.r = right

def is_BST(root):
    if (root):
        if isBST(root.left) is not None:
            return False
        if (prev is not None and root.data <= prev.data):
            return False
        prev = root
        return isBST(root.right)
    return True;
