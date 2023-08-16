class node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_end(self,data):
        if self.head is None:
            self.head = node(data,None)
            return

class Solution:
    #  Should return data of middle node. If linked list is empty, then  -1
    def findMid(self, head):
        # Code here
        # return the value stored in the middle node
        count = 1
        while head!= None:
            count+=1
            print(head)
            head = head.next
        return count
        # return n
        c=0
        while head.next!= None:
            c+=1
            if c==n:
                return head.data
            else :
                head = head.next

ll = LinkedList()
ll.insert_at_end(8)
ll.insert_at_end(9)
ll.insert_at_end(7)
ll.insert_at_end(10)

s = Solution()
print(s.findMid(ll.head))
