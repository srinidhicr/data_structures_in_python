class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

# NON-RECURSIVE
def maximum_element(root):
    if not root:
        return
    queue = []
    queue.append(root)
    max_val = float("-infinity")

    while len(queue)!=0:
        node = queue.pop(0)
        if node.val > max_val:
            max_val = node.val
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    print("NON-RECURSIVE MAX - ", max_val)

def minimum_element(root):
    queue = []
    queue.append(root)

    min_val = float("infinity")
    while( len(queue)!= 0):
        node = queue.pop(0)
        if node.val < min_val:
            min_val = node.val
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    
    print("NON-RECURSIVE MIN - ", min_val)

#RECURSIVE

# To change the value of a global variable inside a function, refer to the variable by using the global keyword
max_val = float("-infinity")
def recursive_max(root):
    global max_val
    if root is None:
        return max_val
    if max_val < root.val:
        max_val = root.val
    recursive_max(root.left)
    recursive_max(root.right)
    return max_val

min_val = float("infinity")
def min_recursive(root):
    global min_val
    if root is None:
        return min_val
    if min_val > root.val:
        min_val = root.val
    min_recursive(root.left)
    min_recursive(root.right)
    return min_val

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(9)
    root.left.left = Node(5)
    root.right.right = Node(4)

    maximum_element(root)
    minimum_element(root)
    max_val = recursive_max(root)
    print("RECURSIVE MAX - ", max_val)
    min_val = min_recursive(root)
    print("RECURSIVE MIN - ", min_val)
