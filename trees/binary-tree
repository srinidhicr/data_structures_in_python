# binary tree have atmost 2 children

"""
DECLARATION
"""

class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

"""
TRAVERSALS 
DFS - Preorder, Postorder, Inorder

Preorder -> parent-left-right
Postorder -> left-right-parent
Inorder -> left-parent-right
"""

def inorder(root):
    if not root:
        return None

    inorder(root.left)
    print(root.val, end = " ")
    inorder(root.right)

def postorder(root):
    if not root:
        return None

    postorder(root.left)
    postorder(root.right)
    print(root.val , end = " ")

def preorder(root):
    if not root:
        return None
    
    print(root.val, end=" ")
    preorder(root.left)
    preorder(root.right)

"""
BFS - Level-order (visit nodes level by level from left to right) - USED QUEUE EFFICIENTLY
"""
def levelorder(root):
    if not root:
        return None
    queue = []

    queue.append(root)
    while queue != []:

        print(queue[0].val, end=" ")
        node = queue.pop(0)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(5)
    root.right.right = Node(4)
    insert(root, 12)

    inorder(root)
    print("\n")
    preorder(root)
    print("\n")
    postorder(root)
    print("\n")
    levelorder(root)



