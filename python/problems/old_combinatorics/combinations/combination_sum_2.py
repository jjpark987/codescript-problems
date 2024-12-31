#!/usr/bin/env python3

from typing import List

# time: O(n * 2^n), space: O(n)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # sort candidates and create result
        candidates.sort()
        result = []

        def backtrack(start, target, path):
            # base cases
            if target == 0:
                result.append(path)
            elif target < 0:
                return
            
            for i in range(start, len(candidates)):
                # if current candidate is greater than target, we STOP the iterations
                if candidates[i] > target:
                    break

                # if current candidate is same as last one, we skip to avoid duplicate combinations
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # move to next target (i + 1)
                backtrack(i + 1, target - candidates[i], path + [candidates[i]])

        backtrack(0, target, [])
        return result

print(Solution().combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8))
print('[[1,1,6],[1,2,5],[1,7],[2,6]]')
print(Solution().combinationSum2(candidates = [2,5,2,1,2], target = 5))
print('[[1,2,2],[5]]')

"""
category: combinatorics
subcategory: combinations
difficulty: medium
image_url_e1: none
image_url_e2: none
image_url_e3: none
title: Combination Sum II

description:
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""