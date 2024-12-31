#!/usr/bin/env python3

import ipdb
from typing import List, Optional
# from functools import reduce
# from collections import deque, defaultdict

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        curr, prev.next = prev.next, None
        while curr:
            temp = curr.next
            if curr.val >= prev.val:
                curr.next = prev
                prev = curr
            curr = temp

        return prev

test = ListNode(5)
test.next = ListNode(2)
test.next.next = ListNode(13)
test.next.next.next = ListNode(3)
test.next.next.next.next = ListNode(8)

print(Solution().removeNodes(head=test))
print('Expected output: [13,8]')

"""
category: linked lists
subcategory: singly
difficulty: medium
image_url_e1: /python/images/remove_nodes_e1.png
image_url_e2: None
title: Remove Nodes From Linked List

description:
You are given the head of a linked list.

Remove every node which has a node with a greater value anywhere to the right side of it.

Return the head of the modified linked list.

 

Example 1:
/python/images/remove_nodes_e1.png

Input: head = [5,2,13,3,8]
Output: [13,8]
Explanation: The nodes that should be removed are 5, 2 and 3.
- Node 13 is to the right of node 5.
- Node 13 is to the right of node 2.
- Node 8 is to the right of node 3.
Example 2:

Input: head = [1,1,1,1]
Output: [1,1,1,1]
Explanation: Every node has value 1, so no nodes are removed.
 

Constraints:

The number of the nodes in the given list is in the range [1, 105].
1 <= Node.val <= 105
"""
