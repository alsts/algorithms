class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(node, key):
    if node is None:  # base case -> insert new node
        return Node(key)

    if key < node.key:
        # insert lower child
        node.left = insert(node.left, key)
    elif key > node.key:
        # insert higher child
        node.right = insert(node.right, key)

    return node


# DFS Examples

def inorder(node):
    if not node:
        return
    inorder(node.left)
    print(node.key)
    inorder(node.right)


def reverse_order(node):
    if not node:
        return
    reverse_order(node.right)
    print(node.key)
    reverse_order(node.left)


def preorder(node):
    if not node:
        return
    print(node.key)
    preorder(node.left)
    preorder(node.right)


def postorder(node):
    if not node:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.key)


root_node = insert(None, 50)
insert(root_node, 30)
insert(root_node, 20)
insert(root_node, 40)
insert(root_node, 70)
insert(root_node, 60)
insert(root_node, 80)

print("############## normal sorted order ##############")
inorder(root_node)
print("############## reversed order ##############")
reverse_order(root_node)
print("############## preorder ##############")
preorder(root_node)
print("############## postorder ##############")
postorder(root_node)
