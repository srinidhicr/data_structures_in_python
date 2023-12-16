class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
    
def inorder(root):
    if not root:
        return None

    inorder(root.left)
    print(root.val, end = " ")
    inorder(root.right)

def insert_ele(root, x):
    queue = []
    queue.append(root)

    while(len(queue)!=0):
        node = queue.pop(0)

        if node.left is not None:
            node.left = Node(x)
            break
        else:
            queue.append(node.left)
        if node.right is not None:
            node.right = Node(x)
            break
        else:
            queue.append(node.right)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(5)
    root.right.right = Node(4)

    inorder(root)

    if insert_ele(root, 11):
        print("Successfully inserted")
    else:
        print("Insertion failed.")

    inorder(root)
    print("\n")