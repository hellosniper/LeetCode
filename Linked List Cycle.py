# Linked List Cycle.py
# Question: Given a linked list, determine if it has a cycle in it.
# Follow up:
# Can you solve it without using extra space?

# Question from: https://oj.leetcode.com/problems/linked-list-cycle/
# Sulotion: # let fast runner to catch up with the slow runner

# Author: DongDing 
# Date: 2014/06/24
# Time complexity:  O(n)
# space complexity:  O(0)
# Tag: linked list   
# Comment: 


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean

    def hasCycle(self, head):
        fast = head
        slow = head
        if head == None:
            return False 
        fast = fast.next

        while (fast != None):
            if fast == slow:
                return True
            if fast.next == None:
                return False
            fast = fast.next.next
            slow = slow.next
        return False
            
