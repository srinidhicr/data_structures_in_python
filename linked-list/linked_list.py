"""a python code of linked list by srinidhi cr
includes creation, insertion and deletion of nodes
- 26 sep 2022
- for leetcode practice"""

#creating a node 
class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        
#creating a linked list
class LinkedList:
    
    #initialise head
    def __init__(self):
        self.head = None

    #traverse linkedlist
    def traverse_ll(self):
        temp = self.head 
        while (temp):
            print(temp.data)
            temp = temp.next
     
    #insert node in beginning
    def insert1(self, data):
        new_node = Node(data)
        new_node.next = self.head 
        self.head = new_node
        
    #insert node after a particular value
    def insert2(self, prev_val, data):
        temp = self.head
        new_node = Node(data)
        while (temp):
            if temp.data == prev_val:
                new_node.next = temp.next 
                temp.next = new_node
            if (temp):
                temp = temp.next
            if temp is None:
                return
            
        """new_node = Node(data)
        temp = self.head
        while(temp):
            if temp is None:
                return
            elif temp.data == prev_val:
                new_node.next = temp.next 
                temp.next = new_node
            else:
                temp = temp.next"""
        
    #insert node at the end
    def insert3(self, data):
        new_node = Node(data)
        #if linked list is empty, attach the new node to it
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while(temp.next):
            temp = temp.next 
        temp.next = new_node    

    #delete a node in the beginning      
    def delete1(self):
        temp = self.head
        self.head = temp.next

    #delete a particular node
    def delete2(self, val):
        temp = self.head
        f = 0
        while(temp.next):
            temp1 = temp
            temp = temp.next
            if temp.data == val:
                temp1.next = temp.next
                temp.next = None   
                f = 1
        if f==0:
            print("Node is not present in linked list.\n")  
            
    #delete a node at the end    
    def delete3(self):
        temp = self.head
        while(temp.next): #temp.next is the last node
            temp1 = temp
            temp = temp.next
        temp1.next = None
        
"""execute following code only if this file is run 
as a script from the command line""" # -> meaning of line 99

if __name__ == '__main__':
    node = LinkedList() #create a linked list object
    node.head = Node(1) #head of linked list
    node1 = Node(2)
    node2 = Node(3)
    
    #linking of nodes
    node.head.next = node1 #link head with 1
    node1.next = node2 #link 1 with 2

    #node.traverse_ll()

    node.insert1(5)

    #node.traverse_ll()

    node.insert2(5, 7)

    node.insert3(9)

    node.traverse_ll()
    print("\n")

    node.delete1()
    print("\n")
    node.traverse_ll()
    node.delete2(3)
    print("\n")
    node.traverse_ll()
    node.delete3()
    print("\n")
    node.traverse_ll()


    
    
    

