# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# def append(self, val):
#     new_node = Node(val)
#     if self.next == None:
#         self.next = new_node
#     else :
#         cur = self.next
#         while cur.next != None:
#             cur = cur.next
#         cur.next = new_node
    
    # def toList(self) -> list:
    #     list = []
    #     cur = self.next
    #     while cur.next:
    #         list.append(cur.val)
    #         cur = cur.next
    #     list.append(cur.val)
    #     return (list)

class Solution:
    def isPalindrome(self, head: ListNode) -> bool: 
        sliceGroup = []

        if head.next == None:
            return False

        cur = head.next
        while cur is not None:
            sliceGroup.append(cur.val)
            cur = cur.next

        print(sliceGroup)
        while len(sliceGroup) > 1:
            if(sliceGroup.pop() != sliceGroup.pop(0)):
                return False
        return True
        

myList = ListNode()
myList.append(1)
myList.append(2)
myList.append(2)
myList.append(1)

print(Solution.isPalindrome(Solution, myList))