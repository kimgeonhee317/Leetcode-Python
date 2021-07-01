# Definition for singly-linked list.

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def addNode(self, node : Node):
        cur = self
        if cur.val == 0:
            cur.val=node.val
            cur.next=node.next   
        else :    
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def printList(self):
        cur = self
        print(cur.val)
        while cur.next != None:
            cur = cur.next
            print(cur.val)
        
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
       
        l1_array = []
        l2_array = []
        l1_int = 0
        l2_int = 0

        cur = l1 # first node
        while cur != None:
            l1_array.append(str(cur.val))
            cur = cur.next
        l1_int = int(''.join(l1_array[::-1]))

        cur = l2 # first node
        while cur != None:
            l2_array.append(str(cur.val))
            cur = cur.next
        l2_int = int(''.join(l2_array[::-1]))
        sum = l1_int+l2_int
        sum_array = list(str(sum))[::-1]

        #make linked list
        listSolution = ListNode()
        for i in range(len(sum_array)):
            listSolution.addNode(Node(sum_array[i]))

        listSolution.printList()
        return listSolution

list1 = ListNode()
list1.addNode(Node(2))
list1.addNode(Node(4))
list1.addNode(Node(3))
list2 = ListNode()
list2.addNode(Node(5))
list2.addNode(Node(6))
list2.addNode(Node(4))
list1.printList()
Solution.addTwoNumbers(Solution, list1, list2)