#!/usr/bin/env python3

import ipdb
from typing import List, Optional
# from collections import Counter, deque, defaultdict
# from functools import reduce

# time: O(nlog(n)), space: O(n)
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        worker.sort()

        max_profit, j, best = 0, 0, 0
        
        for w in worker:
            while j < len(jobs) and w >= jobs[j][0]:
                best = max(best, jobs[j][1])
                j += 1

            max_profit += best
            
        return max_profit

# print(Solution().maxProfitAssignment(difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]))
# print('Expected: 100')
# print(Solution().maxProfitAssignment(difficulty = [85,47,57], profit = [24,66,99], worker = [40,25,25]))
# print('Expected: 0')
# print(Solution().maxProfitAssignment(difficulty = [68,35,52,47,86], profit = [67,17,1,81,3], worker = [92,10,85,84,82]))
# print('Expected: 324')
print(Solution().maxProfitAssignment(difficulty = [66,1,28,73,53,35,45,60,100,44,59,94,27,88,7,18,83,18,72,63], profit = [66,20,84,81,56,40,37,82,53,45,43,96,67,27,12,54,98,19,47,77], worker = [61,33,68,38,63,45,1,10,53,23,66,70,14,51,94,18,28,78,100,16]))
print('Expected: 1392')

"""
category: optimizations
subcategory: maximization
difficulty: medium
image_url_e1: None
image_url_e2: None
title: Most Profit Assigning Work

description:
You have n jobs and m workers. You are given three arrays: difficulty, profit, and worker where:

difficulty[i] and profit[i] are the difficulty and the profit of the ith job, and
worker[j] is the ability of jth worker (i.e., the jth worker can only complete a job with difficulty at most worker[j]).
Every worker can be assigned at most one job, but one job can be completed multiple times.

For example, if three workers attempt the same job that pays $1, then the total profit will be $3. If a worker cannot complete any job, their profit is $0.
Return the maximum profit we can achieve after assigning the workers to the jobs.

 

Example 1:

Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
Output: 100
Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get a profit of [20,20,30,30] separately.
Example 2:

Input: difficulty = [85,47,57], profit = [24,66,99], worker = [40,25,25]
Output: 0
 

Constraints:

n == difficulty.length
n == profit.length
m == worker.length
1 <= n, m <= 104
1 <= difficulty[i], profit[i], worker[i] <= 105
"""