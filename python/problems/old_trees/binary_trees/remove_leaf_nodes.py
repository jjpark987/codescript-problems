#!/usr/bin/env python3

import ipdb
from typing import List, Optional
# from collections import deque, defaultdict
# from functools import reduce

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"TreeNode(val={self.val}, left={repr(self.left)}, right={repr(self.right)})"
    
    @staticmethod
    def list_to_tree(l: list) -> Optional['TreeNode']:
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
    
    @staticmethod
    def tree_to_list(r: Optional['TreeNode']) -> list:
        if not r:
            return []

        result = []
        queue = [r]

        while queue:
            node = queue.pop(0)
            result.append(node.val if node else None)

            if node:
                queue.append(node.left)
                queue.append(node.right)

        while result and result[-1] is None:
            result.pop()

        return result

class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # dfs
        # base case: if root is None, return None
        if not root:
            return
        
        # recursively call method on the left and right children nodes of the root
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        # check if node is leaf and its value matches target
        if not root.left and not root.right and root.val == target:
            return
        
        # return updated root
        return root


print(TreeNode.tree_to_list(Solution().removeLeafNodes(TreeNode.list_to_tree([1,2,3,2,None,2,4]), 2)))
print('Expected: [1, None, 3, None, 4]')
# print(TreeNode.tree_to_list(TreeNode.list_to_tree([1,2,3,2,None,2,4])))

"""
category: trees
subcategory: binary trees
difficulty: medium
image_url_e1: /python/images/remove_leaf_nodes_e1.png
image_url_e2: /python/images/remove_leaf_nodes_e2.png
title: Delete Leaves With a Given Value

description:
Given a binary tree root and an integer target, delete all the leaf nodes with value target.

Note that once you delete a leaf node with value target, if its parent node becomes a leaf node and has the value target, it should also be deleted (you need to continue doing that until you cannot).

 

Example 1:
/python/images/remove_leaf_nodes_e1.png


Input: root = [1,2,3,2,null,2,4], target = 2
Output: [1,null,3,null,4]
Explanation: Leaf nodes in green with value (target = 2) are removed (Picture in left). 
After removing, new nodes become leaf nodes with value (target = 2) (Picture in center).
Example 2:
/python/images/remove_leaf_nodes_e2.png


Input: root = [1,3,3,3,2], target = 3
Output: [1,3,null,null,2]
Example 3:



Input: root = [1,2,null,2,null,2], target = 2
Output: [1]
Explanation: Leaf nodes in green with value (target = 2) are removed at each step.
 

Constraints:

The number of nodes in the tree is in the range [1, 3000].
1 <= Node.val, target <= 1000
"""