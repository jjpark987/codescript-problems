#!/usr/bin/env python3

import ipdb
from typing import List, Optional
# from functools import reduce
# from collections import deque, defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"TreeNode(val={self.val}, left={repr(self.left)}, right={repr(self.right)})"
    
    @staticmethod
    def list_to_tree(l: list) -> 'TreeNode':
        if not l:
            return None
        
        def helper(index):
            if index >= len(l) or l[index] is None:
                return None
            
            node = TreeNode(l[index])
            node.left = helper(2 * index + 1)
            node.right = helper(2 * index + 2)
            return node
        
        return helper(0)

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        # dfs
        if root.val == 0 or root.val == 1:
            return root.val == 1
        elif root.val == 2:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        elif root.val == 3: 
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)
        
        return False


print(Solution().evaluateTree(TreeNode.list_to_tree([3,3,2,0,0,3,2,None,None,None,None,1,3,1,1,None,None,2,1,None,None,None,None,1,1,None,None,None,None,None,None])))
print('Expected: False')
# print(TreeNode.list_to_tree([2,1,3,None,None,0,1]))

"""
category: trees
subcategory: binary trees
difficulty: easy
image_url_e1: /python/images/evaluate_tree_e1.png
image_url_e2: None
title: Evaluate Boolean Binary Tree

description:
You are given the root of a full binary tree with the following properties:

Leaf nodes have either the value 0 or 1, where 0 represents False and 1 represents True.
Non-leaf nodes have either the value 2 or 3, where 2 represents the boolean OR and 3 represents the boolean AND.
The evaluation of a node is as follows:

If the node is a leaf node, the evaluation is the value of the node, i.e. True or False.
Otherwise, evaluate the node's two children and apply the boolean operation of its value with the children's evaluations.
Return the boolean result of evaluating the root node.

A full binary tree is a binary tree where each node has either 0 or 2 children.

A leaf node is a node that has zero children.

 

Example 1:
/python/images/evaluate_tree_e1.png

Input: root = [2,1,3,None,None,0,1]
Output: true
Explanation: The above diagram illustrates the evaluation process.
The AND node evaluates to False AND True = False.
The OR node evaluates to True OR False = True.
The root node evaluates to True, so we return true.
Example 2:

Input: root = [0]
Output: false
Explanation: The root node is a leaf node and it evaluates to false, so we return false.
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 3
Every node has either 0 or 2 children.
Leaf nodes have a value of 0 or 1.
Non-leaf nodes have a value of 2 or 3.
"""