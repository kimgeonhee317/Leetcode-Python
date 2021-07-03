import collections

class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.size = 1000001
        self.table = collections.defaultdict(ListNode)
    
    def print(self) -> None:
        for i in range(self.size):
            cur = self.table[i] # cursur setup
            if cur.value is not None:
                print("("+str(cur.key)+","+str(cur.value)+")")
                while cur.next is not None:
                    cur = cur.next
                    print("("+str(cur.key)+","+str(cur.value)+")")
            else :
                continue

    def put(self, key: int, value: int) -> None:
        index = key % self.size # hash algorithm
        
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return
        else : 
            cur = self.table[index]
            while cur :
                if cur.key == key:
                    cur.value = value
                    return
                if cur.next == None:
                    break
                cur = cur.next
            cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = key % self.size
        cur = self.table[index]      
        while cur :
            if cur.key == key:
                return cur.value
            else:
                cur = cur.next
            return -1 # error

    def remove(self, key: int) -> None:
        index = key % self.size
        cur = self.table[index]

        ## if it's First Node on chaining
        if cur.key == key:
            if cur.next is None :
                self.table[index] = ListNode()
            else : 
                cur = cur.next
            return 
        # it's not first node
        prev = cur
        while cur :
            if cur.key == key: # key matched, we should delete patch the linkedList
                prev.next = cur.next
                return
            prev = cur
            cur = cur.next 

#Your MyHashMap object will be instantiated and called as such:
myHashMap = MyHashMap()
myHashMap.put(100000, 1) # The map is now [[1,1]]
myHashMap.print()

print(myHashMap.get(100000))

myHashMap.put(0, 2) # The map is now [[1,1]]
myHashMap.print()

print(myHashMap.get(0))
