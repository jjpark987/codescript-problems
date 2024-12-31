#!/usr/bin/env python3

from typing import List

# time: O(high), space: O(high)
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * len(days)

        # Base case
        dp[0] = min(costs[0], costs[1], costs[2])

        for i in range(1, len(days)):
            # 1-day pass cost
            cost_1_day = dp[i-1] + costs[0]

            # Find the last day not covered by the 7-day pass
            k_7 = i
            while k_7 >= 0 and days[k_7] >= days[i] - 6:
                k_7 -= 1
            cost_7_day = (dp[k_7] if k_7 >= 0 else 0) + costs[1]

            # Find the last day not covered by the 30-day pass
            k_30 = i
            while k_30 >= 0 and days[k_30] >= days[i] - 29:
                k_30 -= 1
            cost_30_day = (dp[k_30] if k_30 >= 0 else 0) + costs[2]

            # Update dp[i] with the minimum cost so far
            dp[i] = min(cost_1_day, cost_7_day, cost_30_day)

        return dp[-1]

        # Transition
        # 1-day pass: dp[i-1] + cost[0]
        # 7-day pass: dp[i-k] + cost[1]
        # 30-day pass: dp[i-k] + cost [2]

        # Base case
        # dp[0] = min(cost[0], cost[1], cost[2])

        # Boundary
        # 7 or 30 day passes: any costs for days before day 1 is 0
        # this is so that i dont calculate costs for any days before day 1

        # Bottom-up since I need all states to calculate the final answer

"""
category: optimizations
subcategory: processes
difficulty: medium
image_url_e1: none
image_url_e2: none
image_url_e3: none
title: Minimum Cost For Tickets

description:
You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.

Train tickets are sold in three different ways:

a 1-day pass is sold for costs[0] dollars,
a 7-day pass is sold for costs[1] dollars, and
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.

For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.
Return the minimum number of dollars you need to travel every day in the given list of days.

 

Example 1:

Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total, you spent $11 and covered all the days of your travel.
Example 2:

Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
Output: 17
Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
In total, you spent $17 and covered all the days of your travel.
 

Constraints:

1 <= days.length <= 365
1 <= days[i] <= 365
days is in strictly increasing order.
costs.length == 3
1 <= costs[i] <= 1000
"""