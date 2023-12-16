"""
Code does not satisfy for all corner cases, implemented logic on my own for practice.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, data):
        if self.head is None:
            self.head = Node(data)
            self.head.next = self.head
        else:
            curr = Node(data)
            curr.next = self.head
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = curr
            self.head = curr

    def insert_after(self, data, x):
        curr = self.head
        node = Node(x)
        if curr.data == data:
            temp = curr.next
            if temp is None:
                self.head.insert_end()
            else:
                curr.next = node
                node.next = temp
        else:
            while curr.data != data:
                curr = curr.next
            temp = curr.next
            curr.next = node
            node.next = temp

    def insert_end(self, data):
        curr = self.head
        node = Node(data)
        while curr.next != self.head:
            curr = curr.next
        curr.next = node
        node.next = self.head

    def del_node_front(self):
        delnode = self.head
        temp = self.head = delnode.next
        delnode.next = None
        while temp.next != delnode:
            temp = temp.next
        temp.next = self.head

    def del_end(self):
        temp = self.head
        while temp.next.next != self.head:
            temp = temp.next
        temp.next = self.head
        

    def printList(self):
        print(self.head.data, end=" ")
        if self.head.next is not None:
            curr = self.head.next
            while(curr != self.head):
                print(curr.data, end=" ")
                curr = curr.next

    
if __name__ == '__main__':
    circList = LinkedList()

    circList.insert_front(5)
    circList.insert_front(4)
    circList.insert_front(3)
    circList.insert_front(2)


    circList.insert_after(4, 6)
    circList.insert_end(11)

    circList.del_node_front()
    circList.del_end()

    circList.printList()
