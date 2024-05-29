from collections import deque


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


def breadth_first_search(root):
    queue = deque()
    queue.append(root)

    level = 0
    while len(queue) > 0:
        print("level: ", level)
        for i in range(len(queue)):
            curr_node = queue.popleft()
            print(curr_node.key)
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
        level += 1


root_node = insert(None, 4)
insert(root_node, 3)
insert(root_node, 2)
insert(root_node, 6)
insert(root_node, 5)
insert(root_node, 7)

breadth_first_search(root_node)
