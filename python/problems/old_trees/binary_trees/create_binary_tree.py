#!/usr/bin/env python3

from typing import List, Optional

# time: O(n), space: O(1)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        def construct_tree(cur_node_val):
            new_node = TreeNode(cur_node_val)
            if cur_node_val in children_hashmap:
                if children_hashmap[cur_node_val][0] is not None:
                    new_node.left = construct_tree(children_hashmap[cur_node_val][0])
                if children_hashmap[cur_node_val][1] is not None:
                    new_node.right = construct_tree(children_hashmap[cur_node_val][1])
            return new_node

        children_set = set()
        children_hashmap: dict[int, list[int]] = {}

        for parent, child, isleft in descriptions:
            if not parent in children_hashmap:
                children_hashmap[parent] = [None, None]  # left and right
            children_set.add(child)
            target = 0 if isleft else 1
            children_hashmap[parent][target] = child

        for parent in children_hashmap:
            if parent not in children_set:
                head_node_val: int = parent
                break
        head = construct_tree(head_node_val)
        return head

print(Solution().createBinaryTree(descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]))
print('Expected: [50,20,80,15,17,19]')
print(Solution().createBinaryTree(descriptions = [[1,2,1],[2,3,0],[3,4,1]]))
print('Expected: [1,2,null,null,3,4]')

"""
category: trees
subcategory: binary trees
difficulty: medium
image_url_e1: /python/images/create_binary_tree_e1.png
image_url_e2: /python/images/create_binary_tree_e1.png
title: Create Binary Tree From Descriptions

description:
You are given a 2D integer array descriptions where descriptions[i] = [parenti, childi, isLefti] indicates that parenti is the parent of childi in a binary tree of unique values. Furthermore,

If isLefti == 1, then childi is the left child of parenti.
If isLefti == 0, then childi is the right child of parenti.
Construct the binary tree described by descriptions and return its root.

The test cases will be generated such that the binary tree is valid.

 

Example 1:


Input: descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
Output: [50,20,80,15,17,19]
Explanation: The root node is the node with value 50 since it has no parent.
The resulting binary tree is shown in the diagram.
Example 2:


Input: descriptions = [[1,2,1],[2,3,0],[3,4,1]]
Output: [1,2,null,null,3,4]
Explanation: The root node is the node with value 1 since it has no parent.
The resulting binary tree is shown in the diagram.
 

Constraints:

1 <= descriptions.length <= 104
descriptions[i].length == 3
1 <= parenti, childi <= 105
0 <= isLefti <= 1
The binary tree described by descriptions is valid.
"""