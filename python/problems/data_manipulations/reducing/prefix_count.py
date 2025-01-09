#!/usr/bin/env python3

# time: O(nm + k), space: O(nm)
# time: O(nk), space: O(1)
class Solution:
    class Node:
        def __init__(self):
            self.children = {}
            self.prefix_count = 0

    class Trie:
        def __init__(self):
            self.root = Solution.Node()

        def insert(self, word: str) -> None:
            cur_node = self.root
            for c in word:
                if c not in cur_node.children:
                    cur_node.children[c] = Solution.Node()
                cur_node = cur_node.children[c]
                cur_node.prefix_count += 1

        def count_prefixes(self, prefix: str) -> int:
            cur_node = self.root
            for c in prefix:
                if c not in cur_node.children:
                    return 0
                cur_node = cur_node.children[c]
            return cur_node.prefix_count

    def prefixCount(self, words: list[str], pref: str) -> int:
        trie = Solution.Trie()
        for word in words:
            trie.insert(word)
        return trie.count_prefixes(pref)

        # res = 0
        # n = len(pref)
        # for word in words:
        #     if word[:n] == pref:
        #         res += 1

        # return res


"""
category: data manipulations
subcategory: reducing
difficulty: easy
image_url_e1: none
image_url_e2: none
image_url_e3: none
title: Counting Words With a Given Prefix

description:
You are given an array of strings words and a string pref.

Return the number of strings in words that contain pref as a prefix.

A prefix of a string s is any leading contiguous substring of s.

 

Example 1:

Input: words = ["pay","attention","practice","attend"], pref = "at"
Output: 2
Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".
Example 2:

Input: words = ["leetcode","win","loops","success"], pref = "code"
Output: 0
Explanation: There are no strings that contain "code" as a prefix.
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length, pref.length <= 100
words[i] and pref consist of lowercase English letters.
"""