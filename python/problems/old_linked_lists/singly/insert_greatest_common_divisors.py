#!/usr/bin/env python3

from typing import Optional

# time: O(n^2), space: O(1)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_linked_list(array: list[int]) -> Optional[ListNode]:
    if not array:
        return None

    head: ListNode = ListNode(array[0])
    curr: ListNode = head

    for i in range(1, len(array)):
        curr.next = ListNode(array[i])
        curr = curr.next

    return head

def linked_list_to_list(head: ListNode) -> list:
    array: list = []
    curr: Optional[ListNode] = head

    while curr is not None:
        array.append(curr.val)
        curr = curr.next

    return array

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def greatest_common_divsor(x: int, y: int) -> int:
            low, high = min(x, y), max(x, y)
            remainder = high % low
            if remainder == 0:
                return low
            return greatest_common_divsor(low, remainder)

        curr: ListNode = head
        next: Optional[ListNode] = curr.next

        while next:
            val1: int = curr.val
            val2: int = next.val
            gcd: int = greatest_common_divsor(val1, val2)

            insert_node: ListNode = ListNode(val=gcd, next=next)
            curr.next = insert_node

            curr = next
            next = next.next

        return head

print(linked_list_to_list(Solution().insertGreatestCommonDivisors(head = list_to_linked_list([18,6,10,3]))))
print('[18,6,6,2,10,1,3]')
print(linked_list_to_list(Solution().insertGreatestCommonDivisors(head = list_to_linked_list([7]))))
print('[7]')

"""
category: linked_lists
subcategory: singly
difficulty: medium
image_url_e1: /python/images/insert_greatest_common_divisors_e1.jpg
image_url_e2: /python/images/insert_greatest_common_divisors_e2.jpg
image_url_e3: none
title: Insert Greatest Common Divisors in Linked List

description:
Given the head of a linked list head, in which each node contains an integer value.

Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them.

Return the linked list after insertion.

The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

 

Example 1:


Input: head = [18,6,10,3]
Output: [18,6,6,2,10,1,3]
Explanation: The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after inserting the new nodes (nodes in blue are the inserted nodes).
- We insert the greatest common divisor of 18 and 6 = 6 between the 1st and the 2nd nodes.
- We insert the greatest common divisor of 6 and 10 = 2 between the 2nd and the 3rd nodes.
- We insert the greatest common divisor of 10 and 3 = 1 between the 3rd and the 4th nodes.
There are no more adjacent nodes, so we return the linked list.
Example 2:


Input: head = [7]
Output: [7]
Explanation: The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after inserting the new nodes.
There are no pairs of adjacent nodes, so we return the initial linked list.
 

Constraints:

The number of nodes in the list is in the range [1, 5000].
1 <= Node.val <= 1000
"""