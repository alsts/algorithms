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


def search(node, target):
    if node is None:  # base case -> empty node
        return None
    if node.key == target:  # base case -> node found
        return node

    if target < node.key:
        # move lower
        return search(node.left, target)
    else:
        # move higher
        return search(node.right, target)


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
        # node found
        if node.right is None:
            # node has single left child or none
            return node.left  # can be None when no children
        elif node.left is None:
            # node has single right child
            return node.right
        else:
            # node has 2 children - swap node to be removed value with lowest
            min_node = find_min_node(node.right)  # find lowest child in right subtree
            node.key = min_node.key  # swap node value with lowest node value
            node.right = remove(node.right, min_node.key)  # remove lowest child in right subtree

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