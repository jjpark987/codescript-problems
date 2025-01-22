#!/usr/bin/env python

import ipdb
from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        elif n == 2:
            return [0, 1]

        adj_list = {i: [] for i in range(n)}

        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        leaves = {node for node in adj_list if len(adj_list[node]) == 1}

        while n > 2:
            n -= len(leaves)
            new_leaves = set()

            for node in leaves:
                neighbor = adj_list[node].pop()
                adj_list[neighbor].remove(node)
                if len(adj_list[neighbor]) == 1:
                    new_leaves.add(neighbor)

            leaves = new_leaves

        return list(new_leaves)
            
print(Solution().findMinHeightTrees(n=4, edges=[[1,0],[1,2],[1,3]]))
print(Solution().findMinHeightTrees(n=6, edges=[[3,0],[3,1],[3,2],[3,4],[5,4]]))
print(Solution().findMinHeightTrees(n=6, edges=[[0,1],[0,2],[0,3],[3,4],[4,5]]))

"""
category: optimizations
subcategory: structures
difficulty: medium
image_url_e1: /python/images/find_min_height_trees_e1.jpg
image_url_e2: /python/images/find_min_height_trees_e2.jpg
title: Minimum Height Trees

description:
A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

 

Example 1:


Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.
Example 2:


Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]
 

Constraints:

1 <= n <= 2 * 104
edges.length == n - 1
0 <= ai, bi < n
ai != bi
All the pairs (ai, bi) are distinct.
The given input is guaranteed to be a tree and there will be no repeated edges.
"""