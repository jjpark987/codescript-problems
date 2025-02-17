#!/usr/bin/env python3

from typing import List

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        char_count = [0] * 26
        for c in tiles:
            i = ord(c) - ord('A')
            char_count[i] += 1

        return self._find_sequences(char_count)

    def _find_sequences(self, char_count: List[int]) -> int:
        total_count = 0
        for i in range(26):
            if char_count[i] == 0:
                continue
            total_count += 1
            char_count[i] -= 1
            total_count += self._find_sequences(char_count)
            char_count[i] += 1

        return total_count

"""
category: combinatorics
subcategory: counting
difficulty: medium
image_url_e1: none
image_url_e2: none
image_url_e3: none
title: Letter Tile Possibilities

description:
You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.



Example 1:

Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:

Input: tiles = "AAABBC"
Output: 188
Example 3:

Input: tiles = "V"
Output: 1
 

Constraints:

1 <= tiles.length <= 7
tiles consists of uppercase English letters.
"""