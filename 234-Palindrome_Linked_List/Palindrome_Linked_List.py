# Definition for singly-linked list.

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool: 
        sliceGroup = []

        if head.next == None:
            return True
        
        sliceGroup.append(head.val)
        cur = head.next
        while cur is not None:
            sliceGroup.append(cur.val)
            cur = cur.next

        print(sliceGroup)
        while len(sliceGroup) > 1:
            if(sliceGroup.pop() != sliceGroup.pop(0)):
                return False
        return True