# Given a singly linked list, delete middle of the linked list. 
# For example, if given linked list is 1->2->3->4->5 then linked list should be modified to 1->2->4->5.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteMid(head):
    '''
    head:  head of given linkedList
    return: head of resultant llist
    '''
    
    #code here
    if head ==None:
        return None
    if head.next==None:
        return None
    slow=fast=head
    prev=slow
    while(fast!=None and  fast.next!=None):
        fast = fast.next.next
        prev=slow
        slow=slow.next
    prev.next=slow.next
    del slow
    
    return head
    