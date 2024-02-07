"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        # A dummy node to act as the starting point of the merged list
        dummy_ListNode = ListNode()
        # A tail node that will be used to insert nodes into the merged list
        tail_node = dummy_ListNode
        # while both are not wmpty and we aren't at the end of the list
        while list1 and list2:
            # if the starting value of list1 equal or smaller
            if list1.val <= list2.val:
                # make it become the next node in the appended list
                tail_node.next = list1
                #  move list1 to its next node
                list1 = list1.next
            else:
                # Otherwise, attach list2 node to the tail node
                tail_node.next = list2
                # move list2 to its next node
                list2 = list2.next
            # Move the tail pointer forward to the newly added node
            tail_node = tail_node.next
        # At the end of this loop, at least one of the lists is empty
        # Attach the non-empty list to the end of the merged list
        tail_node.next = list1 if list1 is not None else list2
        # Return the next of dummy node as tasks required (the head of the merged list)
        return dummy_ListNode.next
