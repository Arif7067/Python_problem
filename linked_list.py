class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node
    
    def printing(self):
        if self.head == None:
            print("Thiss list is empty")
            return
        
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+'-->'
            itr = itr.next
        print(llstr)
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def inser_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    def get_length(self):
        count =0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count
    
    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid index")
        if index ==0:
            self.head = self.head.next
            return
        count =0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count+=1
        # return
    def insert_at(self,index, data):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid index")
        if index ==0:
            self.insert_at_beginning(data)
            return
        count =0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data,itr.next)
                itr.next = node
                break
            itr = itr.next
            count+=1

if __name__ == '__main__':
    ll = LinkedList()
    # ll.insert_at_beginning(5)
    # ll.insert_at_beginning(89)
    # ll.insert_at_end(99)
    ll.inser_values(["bananas","apples","mangos","grapes"])
    ll.printing()
    ll.remove_at(2)
    ll.printing()
    ll.insert_at(0,"potatoes")
    ll.printing()
    ll.insert_at(3,"Kerala")
    ll.printing()
    print(ll.get_length())