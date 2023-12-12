class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

#RECURSIVE METHOD
def search_recursive(root, x):
    if root is None:
        return False
    if root.val == x:
        return True
    search_recursive(root.left, x)
    search_recursive(root.right, x)

# BFS - NON-RECURSIVE METHOD
def search_ele(root, x):
    queue = []
    queue.append(root)

    while(len(queue)!=0):
        node = queue.pop(0)
        if node.val == x:
            return True
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return False

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(9)
    root.left.left = Node(5)
    root.right.right = Node(4)

    x = int(input("Enter element to search for: "))
    if search_ele(root, x):
        print("NON-RECURSIVE - Element is present.")
    else:
        print("NON-RECURSIVE - Element is absent.")

    if search_recursive(root, x):
        print("RECURSIVE - Element is present.")
    else:
        print("RECURSIVE - Element is absent.")
