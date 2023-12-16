"""
Find kth node from end from the linked list - efficient implementation
2 pts - ptr1, ptr2
move ptr2 for n moves.
after n moves, move ptr1 and ptr2 simultaneously till ptr2 reaches null
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

    def removeNode(self, k):
        ptr1 = ptr2 = self.head
        while(k > 0 and ptr2 is not None):
            ptr2 = ptr2.next
            k -= 1
        if ptr2 is not None:
            while(ptr2 is not None):
                ptr1 = ptr1.next
                ptr2 = ptr2.next
            ptr1 = ptr1.next
        print(ptr1.data)
        

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
    linkedlist.insert(14)
    linkedlist.insert(8)
    linkedlist.insert(6)

    #linkedlist.printList()

    k = 4 #kth node to be found from the back
    linkedlist.removeNode(k)

