#!/usr/bin/env python3

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def list_to_tree(array: list) -> TreeNode:
    if not array:
        return
    
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

# time: O(n), space: O(n)
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        # Find all leaf nodes
        def dfs(node):
            if node is None:
                return
            
            if node.left is None and node.right is None:
                leaf_nodes.append(node)

            dfs(node.left)
            dfs(node.right)

        # Compute distances from root
        def compute_distances(node, depth):
            if node is None:
                return
            
            distances[node] = depth

            compute_distances(node.left, depth + 1)
            compute_distances(node.right, depth + 1)

        # Find parent pointers
        def find_parents(node, parent):
            if node is None:
                return
            
            parents[node] = parent

            find_parents(node.left, node)
            find_parents(node.right, node)

        # Find lowest common ancestor
        def find_lca(u, v):
            ancestors_u = set()

            while u:
                ancestors_u.add(u)
                u = parents[u]

            while v:
                if v in ancestors_u:
                    return v
                v = parents[v]

        # Count good leaf node pairs
        def count_good_pairs(leaf_nodes, distance):
            good_pairs = 0

            for i in range(len(leaf_nodes)):
                for j in range(i + 1, len(leaf_nodes)):
                    u = leaf_nodes[i]
                    v = leaf_nodes[j]
                    lca = find_lca(u, v)
                    dist = distances[u] + distances[v] - 2 * distances[lca]

                    if dist <= distance:
                        good_pairs += 1
            
            return good_pairs
        
        leaf_nodes = []
        distances = {}
        parents = {}

        dfs(root)
        compute_distances(root, 0)
        find_parents(root, None)

        return count_good_pairs(leaf_nodes, distance)

print(Solution().countPairs(list_to_tree([1,2,3,None,4]), 3))
print('Expected: 1')
print(Solution().countPairs(list_to_tree([1,2,3,4,5,6,7]), 3))
print('Expected: 2')

"""
category: trees
subcategory: binary trees
difficulty: medium
image_url_e1: /python/images/count_pairs_e1.png
image_url_e2: /python/images/count_pairs_e2.png
image_url_e3: none
title: Number of Good Leaf Nodes Pairs

description:
You are given the root of a binary tree and an integer distance. A pair of two different leaf nodes of a binary tree is said to be good if the length of the shortest path between them is less than or equal to distance.

Return the number of good leaf node pairs in the tree.

 

Example 1:


Input: root = [1,2,3,null,4], distance = 3
Output: 1
Explanation: The leaf nodes of the tree are 3 and 4 and the length of the shortest path between them is 3. This is the only good pair.
Example 2:


Input: root = [1,2,3,4,5,6,7], distance = 3
Output: 2
Explanation: The good pairs are [4,5] and [6,7] with shortest path = 2. The pair [4,6] is not good because the length of ther shortest path between them is 4.
Example 3:

Input: root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3
Output: 1
Explanation: The only good pair is [2,5].
"""