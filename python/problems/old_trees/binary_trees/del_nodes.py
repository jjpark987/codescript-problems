#!/usr/bin/env python3

from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def list_to_tree(array: list) -> TreeNode:
    if not array:
        return None
    
    root = TreeNode(array[0])
    queue = deque([root])
    i = 1

    while i < len(array):
        current = queue.popleft()

        if array[i] is not None:
            current.left = TreeNode(array[i])
            queue.append(current.left)
        i += 1

        if array[i] is not None and i < len(array):
            current.right = TreeNode(array[i])
            queue.append(current.right)
        i += 1

    return root

def tree_to_list(root: Optional[TreeNode]) -> list:
    if root is None:
        return []
    
    array = []
    queue = deque([root])

    while queue:
        current = queue.popleft()

        if current:
            array.append(current.val)
            queue.append(current.left)
            queue.append(current.right)
        else:
            array.append(None)

    while array and array[-1] is None:
        array.pop()

    return array

def roots_to_list(roots: List[TreeNode]) -> list:
    array = []

    for root in roots:
        array.append(tree_to_list(root))

    return array

# time: O(n), space: O(n)
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        delete_set = set(to_delete)
        forest = []

        def dfs(node):
            if node is None:
                return None
            
            node.left = dfs(node.left)
            node.right = dfs(node.right)

            if node.val in delete_set:
                if node.left:
                    forest.append(node.left)
                if node.right:
                    forest.append(node.right)
                return None
            
            return node
            
        root = dfs(root)
            
        if root:
            forest.append(root)

        return forest
    
print(roots_to_list(Solution().delNodes(list_to_tree([1,2,3,4,5,6,7]), to_delete = [3,5])))
print('Expected: [[1,2,None,4],[6],[7]]')
print(roots_to_list(Solution().delNodes(list_to_tree([1,2,4,None,3]), to_delete = [3])))
print('Expected: [[1,2,4]]')

"""
category: trees
subcategory: binary trees
difficulty: medium
image_url_e1: /python/images/del_nodes_e1.png
image_url_e2: none
image_url_e3: none
title: Delete Nodes And Return Forest

description:
Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest. You may return the result in any order.

 

Example 1:


Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
Example 2:

Input: root = [1,2,4,null,3], to_delete = [3]
Output: [[1,2,4]]
 

Constraints:

The number of nodes in the given tree is at most 1000.
Each node has a distinct value between 1 and 1000.
to_delete.length <= 1000
to_delete contains distinct values between 1 and 1000.
"""