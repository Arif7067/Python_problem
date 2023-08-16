# Given a linked list consisting of L nodes and given a number N. The task is to find the Nth node from the end of the linked list.


#Function to find the data of nth node from the end of a linked list
def getNthFromLast(head,n):
    #code here
    t=head
    count =0
    while t!=None:
        t=t.next
        count+=1
    if n>count:
        return -1
    n=count-n+1
    while n>0:
        if n==1:
            return head.data
        head=head.next
        n-=1
        
    return -1