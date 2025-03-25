#!/usr/bin/env python3

from typing import List

class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x_axis = [[startx, endx] for startx, _, endx, _ in rectangles]
        y_axis = [[starty, endy] for _, starty, _, endy in rectangles]
        x_axis.sort(key=lambda x: (x[0], -x[1]))
        y_axis.sort(key=lambda y: (y[0], -y[1]))

        def can_be_cut(axis):
            prev = ()
            sections = []
            for start, end in axis:
                if not prev:
                    prev = (start, end)
                    sections.append([start, end])
                    continue
                if start < prev[1] and end <= prev[1]:
                    continue
                if start < prev[1] and end > prev[1]:
                    prev = (prev[0], end)
                    sections[-1] = [prev[0], end]
                else:
                    prev = (start, end)
                    sections.append([start, end])

            if len(sections) >= 3:
                return True

            return False

        return can_be_cut(x_axis) or can_be_cut(y_axis)

'''
category: data manipulations
subcategory: reducing
difficulty: medium
image_path_e1: check_if_grid_can_be_cut_into_sections_e1.png
image_path_e2: check_if_grid_can_be_cut_into_sections_e2.png
image_path_e3: none
title: Check if Grid can be Cut into Sections

description:
You are given an integer n representing the dimensions of an n x n grid, with the origin at the bottom-left corner of the grid. You are also given a 2D array of coordinates rectangles, where rectangles[i] is in the form [startx, starty, endx, endy], representing a rectangle on the grid. Each rectangle is defined as follows:

(startx, starty): The bottom-left corner of the rectangle.
(endx, endy): The top-right corner of the rectangle.
Note that the rectangles do not overlap. Your task is to determine if it is possible to make either two horizontal or two vertical cuts on the grid such that:

Each of the three resulting sections formed by the cuts contains at least one rectangle.
Every rectangle belongs to exactly one section.
Return true if such cuts can be made; otherwise, return false.

 

Example 1:

Input: n = 5, rectangles = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]

Output: true

Explanation:



The grid is shown in the diagram. We can make horizontal cuts at y = 2 and y = 4. Hence, output is true.

Example 2:

Input: n = 4, rectangles = [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]

Output: true

Explanation:



We can make vertical cuts at x = 2 and x = 3. Hence, output is true.

Example 3:

Input: n = 4, rectangles = [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]

Output: false

Explanation:

We cannot make two horizontal or two vertical cuts that satisfy the conditions. Hence, output is false.

 

Constraints:

3 <= n <= 109
3 <= rectangles.length <= 105
0 <= rectangles[i][0] < rectangles[i][2] <= n
0 <= rectangles[i][1] < rectangles[i][3] <= n
No two rectangles overlap.
'''