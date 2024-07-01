class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# Recursive
def preorder_recursive(node):
    if not node:
        return
    print(node.key)
    preorder_recursive(node.left)
    preorder_recursive(node.right)


# Iterative
def preorder_iterative(node):
    stack = []
    curr = node

    while curr or stack:
        if curr:
            print(curr.key)
            if curr.right:
                # append right child for further processing
                stack.append(curr.right)
            curr = curr.left  # always traverse left
        else:
            # no left child -> pop right one from the stack
            curr = stack.pop()


root_node = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(4)
node_5 = Node(5)

root_node.left = node_2
root_node.right = node_3
node_2.left = node_4
node_3.right = node_5

preorder_iterative(root_node)
preorder_recursive(root_node)
