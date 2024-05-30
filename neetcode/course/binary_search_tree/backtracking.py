class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def can_reach_leaf_node(node, path):
    if not node or node.key == 0:  # base case -> not leaf or 0
        return False

    path.append(node.key)  # node found that can be part of path

    if not node.left and not node.right:  # base case -> leaf node found
        return True

    # not leaf node -> recursively traverse to left subtree, then right
    if can_reach_leaf_node(node.left, path):
        return True
    if can_reach_leaf_node(node.right, path):
        return True

    # no leaf node found or encountered 0 in left or right subtree
    # remove node as it is not satisfying the path
    path.pop()
    return False


# prepare the Tree:
root_node = Node(4)
left_top_node = Node(0)
left_top_node.right = Node(7)

right_top_node = Node(1)
right_left_node = Node(3)
right_left_node.right = Node(0)
right_top_node.left = right_left_node
right_top_node.right = Node(2)

root_node.left = left_top_node
root_node.right = right_top_node

# Determine if path exists from the root of the tree to a left node.
# It may not contain any zeroes!!!

path_to_find = []
print(can_reach_leaf_node(root_node, path_to_find))
print(path_to_find)