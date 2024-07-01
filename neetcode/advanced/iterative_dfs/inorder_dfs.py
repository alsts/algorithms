class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# Recursive
def inorder_recursive(node):
    if not node:
        return
    inorder_recursive(node.left)
    print(node.key)
    inorder_recursive(node.right)


# Iterative
def inorder_iterative(node):
    stack = []
    curr = node

    while curr or stack:
        if curr:
            # node present -> append to stack and check left child
            stack.append(curr)
            curr = curr.left
        else:
            # node not present -> reached left-most leaf
            curr = stack.pop()
            print(curr.key)
            curr = curr.right  # check if has right child


root_node = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(4)
node_5 = Node(5)

root_node.left = node_2
root_node.right = node_3
node_2.left = node_4
node_3.right = node_5

inorder_iterative(root_node)
inorder_recursive(root_node)
