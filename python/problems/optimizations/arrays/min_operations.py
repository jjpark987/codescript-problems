#!/usr/bin/env python3

from typing import List

# time: O(n), space: O(n)
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        def calculate_contributions(boxes: str, n: int, direction: int) -> List[int]:
            operations = [0] * n
            current_operations = 0
            ball_count = 0

            indices = range(n) if direction == 1 else range(n - 1, -1, -1)

            for i in indices:
                operations[i] = current_operations
                if boxes[i] == '1':
                    ball_count += 1
                current_operations += ball_count

            return operations

        n = len(boxes)
        left_operations = calculate_contributions(boxes, n, direction=1)
        right_operations = calculate_contributions(boxes, n, direction=-1)
        
        return [left + right for left, right in zip(left_operations, right_operations)]

"""
category: optimizations
subcategory: arrays
difficulty: medium
image_url_e1: none
image_url_e2: none
image_url_e3: none
title: Minimum Number of Operations to Move All Balls to Each Box

description:
You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the ith box is empty, and '1' if it contains one ball.

In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j if abs(i - j) == 1. Note that after doing so, there may be more than one ball in some boxes.

Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls to the ith box.

Each answer[i] is calculated considering the initial state of the boxes.

 

Example 1:

Input: boxes = "110"
Output: [1,1,3]
Explanation: The answer for each box is as follows:
1) First box: you will have to move one ball from the second box to the first box in one operation.
2) Second box: you will have to move one ball from the first box to the second box in one operation.
3) Third box: you will have to move one ball from the first box to the third box in two operations, and move one ball from the second box to the third box in one operation.
Example 2:

Input: boxes = "001011"
Output: [11,8,5,4,3,4]
 

Constraints:

n == boxes.length
1 <= n <= 2000
boxes[i] is either '0' or '1'
"""