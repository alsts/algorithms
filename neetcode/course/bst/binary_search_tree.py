class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(node, key):
    if node is None:  # base case -> insertion slot found
        return Node(key)

    if key < node.key:
        node.left = insert(node.left, key)  # insert lower child
    elif key > node.key:
        node.right = insert(node.right, key)  # insert higher child

    return node


def search(node, search_key):
    if node is None:  # base case -> empty node
        return None
    if node.key == search_key:  # base case -> node found
        return node

    if search_key < node.key:
        return search(node.left, search_key)  # lower
    else:
        return search(node.right, search_key)  # higher


def find_min_node(node):
    curr = node
    while curr and curr.left:
        curr = curr.left
    return curr


def remove(node, key):
    if node is None:
        return None

    if key < node.key:
        node.left = remove(node.left, key)
    elif key > node.key:
        node.right = remove(node.right, key)
    else:
        # node has 2 children
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        else:
            min_node = find_min_node(node.right)
            node.key = min_node.key
            node.right = remove(node.right, min_node.key)

    return node


root_node = insert(None, 50)
insert(root_node, 30)
insert(root_node, 20)
insert(root_node, 40)
insert(root_node, 70)
insert(root_node, 60)
insert(root_node, 80)

print("Searching for key: 6 in BST: ", search(root_node, 6))
print("Searching for key: 60 in BST: ", search(root_node, 60).key)

remove(root_node, 40)