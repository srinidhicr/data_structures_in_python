"""
Boilerplate code for single linked list.
"""

class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            temp = self.head
            while(temp.next is not None):
                temp = temp.next
            temp.next = Node(data)

    def printList(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next


if __name__ == '__main__':
    linkedlist = LinkedList()
    linkedlist.insert(5)
    linkedlist.insert(7)
    linkedlist.insert(11)
    linkedlist.insert(2)
    linkedlist.insert(4)

    linkedlist.printList()

