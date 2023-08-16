# Given a singly linked list of N nodes.
# The task is to find the middle of the linked list. For example, if the linked list is
# 1-> 2->3->4->5, then the middle node of the list is 3.
# If there are two middle nodes(in case, when N is even), print the second middle element.
# For example, if the linked list given is 1->2->3->4->5->6, then the middle node of the list is 4.



class node:
    def __init__(data):
        self.data = data
        self.next = None

class Solution:
    def findMid(self, head):
        count = 0
        t=head
        while t!= None:
            count+=1
            t = t.next
        n=count//2
        while n!= 0:
            head= head.next
            n-=1
        return head.data