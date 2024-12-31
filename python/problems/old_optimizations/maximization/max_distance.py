#!/usr/bin/env python3

from typing import List, Optional
# from collections import Counter, deque, defaultdict
# from functools import reduce

# time: O(nlog(n) + nlog(max(position) - min(position))), space: O(1)
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # use a binary search to narrow down the max distance
        # for each guess, starting with mid, iterate through position
            # check if distance between current and last is equal or greater, if it is then place ball and update last
        # if balls placed is equal or greater than m then set answer and try with greater distance interval (adjust left to be mid + 1)
        # if balls placed is less than m then try again with smaller distance interval (adjust right to be mid - 1)
        # return answer
        position.sort()
        left = 1
        right = position[-1]
        result = -1

        while left <= right:
            mid = left + (right - left) // 2
            last_pos = position[0]
            balls = 1

            for i in range(1, len(position)):
                if position[i] - last_pos >= mid:
                    last_pos = position[i]
                    balls += 1
            
            if balls >= m:
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result

print(Solution().maxDistance(position = [1,2,3,4,7], m = 3))
print('Expected: 3')
print(Solution().maxDistance(position = [5,4,3,2,1,1000000000], m = 2))
print('Expected: 999999999')
print(Solution().maxDistance(position = [1,1000000000], m = 2))
print('Expected: 999999999')

"""
category: optimizations
subcategory: maximization
difficulty: medium
image_url_e1: /python/images/max_distance_e1.jpg
image_url_e2: None
title: Magnetic Force Between Two Balls

description:
In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket. Rick has n empty baskets, the ith basket is at position[i], Morty has m balls and needs to distribute the balls into the baskets such that the minimum magnetic force between any two balls is maximum.

Rick stated that magnetic force between two different balls at positions x and y is |x - y|.

Given the integer array position and the integer m. Return the required force.

 

Example 1:
/python/images/max_distance_e1.jpg

Input: position = [1,2,3,4,7], m = 3
Output: 3
Explanation: Distributing the 3 balls into baskets 1, 4 and 7 will make the magnetic force between ball pairs [3, 3, 6]. The minimum magnetic force is 3. We cannot achieve a larger minimum magnetic force than 3.
Example 2:

Input: position = [5,4,3,2,1,1000000000], m = 2
Output: 999999999
Explanation: We can use baskets 1 and 1000000000.
 

Constraints:

n == position.length
2 <= n <= 105
1 <= position[i] <= 109
All integers in position are distinct.
2 <= m <= position.length
"""