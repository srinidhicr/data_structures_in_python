"""a python code of doubly linked list
includes creation, insertion and deletion of nodes
- for leetcode practice"""

class Node:
        def __init__(self, data) -> None:
            self.data = data
            self.next = None
            self.prev = None

class LinkedList:
    
    #initialise head
    def __init__(self):
        self.head = None

    
    """
    def insert_front(self, data):
        if self.head == None:
             self.head = Node(data)
        newNode = Node(data)
        newNode.next = self.head
        newNode.prev = None
        self.head.prev = newNode
        self.head = newNode #change the head to new node
    """

    
    def insert_front(self, data):
        #check if node has an initial el
        if self.head is None:
            self.head = Node(data)
        # if not add to existing list
        else:
            node = Node(data)
            node.next = self.head
            node.prev = None
            self.head.prev = node
            self.head = node
         
    #insert x after data
    def insert_after(self, data, x):
        newNode = Node(x)
        temp = self.head

        while(temp.data != data):
            temp = temp.next
        newNode.next = temp.next
        temp.next.prev = newNode
        temp.next = newNode
        newNode.prev = temp

    def insert_end(self, data):
        newNode = Node(data)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = newNode
        newNode.prev = temp
        
    def del_front(self):
        temp = self.head.next
        temp.prev = None
        self.head = temp

    def del_a_val(self, val):
        curr = self.head
        while curr.data != val:
            curr = curr.next
        prevcurr = curr.prev
        prevcurr.next = curr.next
        curr.prev = None

    def del_last_node(self):
        temp = self.head
        while(temp.next is not None):
            temp = temp.next
        prevcurr = temp.prev
        prevcurr.next = None
        temp.prev = None
        
    def print(self):
        curr = node.head
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next

if __name__ == '__main__':
    node = LinkedList() #create a linked list object
    node.insert_front(5)
    node.insert_end(6)
    node.insert_after(5, 3)

    node.print()

    #node.del_front()
    print("\n")
    node.print()
    print("\n")
    #node.del_a_val(3)
    node.print()
    print("\n")
    #node.del_last_node()
    node.print()



    #LINKING DOUBLY LL
    

        
        