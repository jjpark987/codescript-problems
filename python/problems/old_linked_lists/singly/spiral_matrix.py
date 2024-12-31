#!/usr/bin/env python3

from typing import List, Optional, Tuple

# time: O(n), space: O(n)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_linked_list(array: list[int]) -> Optional[ListNode]:
    if not array:
        return None

    head: ListNode = ListNode(array[0])
    curr: ListNode = head

    for i in range(1, len(array)):
        curr.next = ListNode(array[i])
        curr = curr.next

    return head

# def linked_list_to_list(head: ListNode) -> list:
#     array: list = []
#     curr: Optional[ListNode] = head

#     while curr is not None:
#         array.append(curr.val)
#         curr = curr.next

#     return array

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        if head is None:
            return []

        # Initialize the result matrix and current position
        result: List[List[int]] = [[None] * n for _ in range(m)]
        position: Tuple[int, int] = (0, 0)
        
        # Directional mappings
        directions: List[Tuple[int, int]] = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # e, s, w, n
        dir_index: int = 0  # Start facing east
        curr_node: Optional[ListNode] = head
        
        # Fill the matrix in a spiral order
        for _ in range(m * n):
            # Assign current node's value to the result matrix
            result[position[0]][position[1]] = curr_node.val if curr_node else -1
            curr_node = curr_node.next if curr_node else None

            # Determine the next position
            next_position = (position[0] + directions[dir_index][0], position[1] + directions[dir_index][1])

            # Check if next position is valid
            if self.is_valid_position(next_position, m, n, result):
                position = next_position
            else:
                dir_index = (dir_index + 1) % 4  # Change direction
                position = (position[0] + directions[dir_index][0], position[1] + directions[dir_index][1])

        return result

    def is_valid_position(self, pos: Tuple[int, int], m: int, n: int, result: List[List[int]]) -> bool:
        """Check if the next position is within bounds and not yet filled."""
        return (0 <= pos[0] < m and 
                0 <= pos[1] < n and 
                result[pos[0]][pos[1]] is None)

print(Solution().spiralMatrix(m = 3, n = 5, head = list_to_linked_list([3,0,2,6,8,1,7,9,4,2,5,5,0])))
print('[[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]')
print(Solution().spiralMatrix(m = 1, n = 4, head = list_to_linked_list([0,1,2])))
print('[[0,1,2,-1]]')

"""
category: linked_lists
subcategory: singly
difficulty: medium
image_url_e1: /python/images/spiral_matrix_e1.jpg
image_url_e2: /python/images/spiral_matrix_e2.jpg
image_url_e3: none
title: Spiral Matrix IV

description:
You are given two integers m and n, which represent the dimensions of a matrix.

You are also given the head of a linked list of integers.

Generate an m x n matrix that contains the integers in the linked list presented in spiral order (clockwise), starting from the top-left of the matrix. If there are remaining empty spaces, fill them with -1.

Return the generated matrix.

 

Example 1:


Input: m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
Output: [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]
Explanation: The diagram above shows how the values are printed in the matrix.
Note that the remaining spaces in the matrix are filled with -1.
Example 2:


Input: m = 1, n = 4, head = [0,1,2]
Output: [[0,1,2,-1]]
Explanation: The diagram above shows how the values are printed from left to right in the matrix.
The last space in the matrix is set to -1.
 

Constraints:

1 <= m, n <= 105
1 <= m * n <= 105
The number of nodes in the list is in the range [1, m * n].
0 <= Node.val <= 1000
"""