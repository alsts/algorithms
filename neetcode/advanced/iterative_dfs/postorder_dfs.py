class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# Recursive
def postorder_recursive(node):
    if not node:
        return
    postorder_recursive(node.left)
    postorder_recursive(node.right)
    print(node.key)


# Iterative
def postorder_iterative(node):
    stack = [node]
    visit = [False]

    while stack:
        curr, visited = stack.pop(), visit.pop()

        if curr:
            if visited:
                print(curr.key)
            else:
                stack.append(curr)
                visit.append(True)

                if curr.right:
                    # the right child/subtree would be processed second
                    stack.append(curr.right)
                    visit.append(False)

                if curr.left:
                    # the left child/subtree would be processed first
                    stack.append(curr.left)
                    visit.append(False)


root_node = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(4)
node_5 = Node(5)

root_node.left = node_2
root_node.right = node_3
node_2.left = node_4
node_3.right = node_5

postorder_iterative(root_node)
postorder_recursive(root_node)
