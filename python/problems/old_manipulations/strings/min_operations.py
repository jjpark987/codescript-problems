#!/usr/bin/env python3

from typing import List
# from collections import Counter, deque, defaultdict
# from functools import reduce

# time: O(n), space: O(1)
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        result: int = 0 

        for operation in logs:
            if operation == '../':
                if result > 0:
                    result -= 1
            elif operation != './':
                result += 1
        
        return result

print(Solution().minOperations(logs = ["d1/","d2/","../","d21/","./"]))
print('Expected: 2')
print(Solution().minOperations(logs = ["d1/","d2/","./","d3/","../","d31/"]))
print('Expected: 3')
print(Solution().minOperations(logs = ["d1/","../","../","../"]))
print('Expected: 0')

"""
category: manipulations
subcategory: strings
difficulty: easy
image_url_e1: /python/images/min_operations_e1.png
image_url_e2: /python/images/min_operations_e2.png
title: Crawler Log Folder

description:
The Leetcode file system keeps a log each time some user performs a change folder operation.

The operations are described below:

"../" : Move to the parent folder of the current folder. (If you are already in the main folder, remain in the same folder).
"./" : Remain in the same folder.
"x/" : Move to the child folder named x (This folder is guaranteed to always exist).
You are given a list of strings logs where logs[i] is the operation performed by the user at the ith step.

The file system starts in the main folder, then the operations in logs are performed.

Return the minimum number of operations needed to go back to the main folder after the change folder operations.

 

Example 1:
/python/images/min_operations_e1.png


Input: logs = ["d1/","d2/","../","d21/","./"]
Output: 2
Explanation: Use this change folder operation "../" 2 times and go back to the main folder.
Example 2:
/python/images/min_operations_e2.png


Input: logs = ["d1/","d2/","./","d3/","../","d31/"]
Output: 3
Example 3:

Input: logs = ["d1/","../","../","../"]
Output: 0
 

Constraints:

1 <= logs.length <= 103
2 <= logs[i].length <= 10
logs[i] contains lowercase English letters, digits, '.', and '/'.
logs[i] follows the format described in the statement.
Folder names consist of lowercase English letters and digits.
"""