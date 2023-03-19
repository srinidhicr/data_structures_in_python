"""a python code implementation of stack by srinidhi cr
includes operations push, pop, peek and display
- 20 oct 2022
- for leetcode practice"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    #check whether stack is empty
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

    #push elements to the stack
    def push(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode

    #pop the element at the top of the stack
    def pop(self):
        if self.isEmpty():
            return None
        else:
            temp = self.head
            self.head= self.head.next
            temp.next = None
            return temp.data

    def peek(self):
        if self.isEmpty():
            return None

        else:
            return (self.head).data

    def display(self):
        iternode = self.head
        if self.isEmpty():
            print("Stack Underflow")
 
        else:
 
            while(iternode != None):
 
                print(iternode.data, end = "")
                iternode = iternode.next
                if(iternode != None):
                    print(" -> ", end = "")
            return

if __name__ == '__main__':
    meraStack = Stack()

    meraStack.push(12)
    meraStack.push(5)
    meraStack.push(17)
    meraStack.push(48)
    meraStack.push(66)
    meraStack.push(32)

    meraStack.display()
    print("\n")
    meraStack.pop()
    meraStack.pop()

    meraStack.display()
    print("\n")
    print(meraStack.peek())

    
            

