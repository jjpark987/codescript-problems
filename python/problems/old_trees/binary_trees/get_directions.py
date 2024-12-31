#!/usr/bin/env python3

from typing import Optional, List
from collections import deque

# time: O(n), space: O(1)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def list_to_tree(list):
        if not list:
            return None
        
        root = TreeNode(list[0])
        queue = deque([root])
        i = 1
        
        while queue and i < len(list):
            current = queue.popleft()
            
            if list[i] is not None:
                current.left = TreeNode(list[i])
                queue.append(current.left)
            i += 1
            
            if list[i] is not None:
                current.right = TreeNode(list[i])
                queue.append(current.right)
            i += 1
            
        return root
    
    # def tree_to_list(self):
    #     result = []
    #     queue = deque([self])

    #     while queue:
    #         node = queue.popleft()

    #         if node:
    #             result.append(node.val)
    #             queue.append(node.left)
    #             queue.append(node.right)
    #         else:
    #             result.append(None)

    #     while result and result[-1] is None:
    #         result.pop()

    #     return result

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def find(n: TreeNode, val: int, path: List[str]) -> bool:
            if n.val == val:
                return True
            if n.left and find(n.left, val, path):
                path += "L"
            elif n.right and find(n.right, val, path):
                path += "R"
            return path

        s, d = [], []
        find(root, startValue, s)
        find(root, destValue, d)
        
        while len(s) and len(d) and s[-1] == d[-1]:
            s.pop()
            d.pop()
        return "".join("U" * len(s)) + "".join(reversed(d))

print(Solution().getDirections(root = TreeNode().list_to_tree([5,1,2,3,None,6,4]), startValue = 3, destValue = 6))
print('Expected: "UURL"')
print(Solution().getDirections(root = TreeNode().list_to_tree([2,1]), startValue = 2, destValue = 1))
print('Expected: "L"')

"""
category: trees
subcategory: binary trees
difficulty: medium
image_url_e1: /python/images/get_directions_e1.png
image_url_e2: /python/images/get_directions_e2.png
title: Step-By-Step Directions From a Binary Tree Node to Another

description:
You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are also given an integer startValue representing the value of the start node s, and a different integer destValue representing the value of the destination node t.

Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:

'L' means to go from a node to its left child node.
'R' means to go from a node to its right child node.
'U' means to go from a node to its parent node.
Return the step-by-step directions of the shortest path from node s to node t.

 

Example 1:


Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
Output: "UURL"
Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.
Example 2:


Input: root = [2,1], startValue = 2, destValue = 1
Output: "L"
Explanation: The shortest path is: 2 → 1.
 

Constraints:

The number of nodes in the tree is n.
2 <= n <= 105
1 <= Node.val <= n
All the values in the tree are unique.
1 <= startValue, destValue <= n
startValue != destValue
"""