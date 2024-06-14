class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


def find_middle(head):
    fast, slow = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(4)
node_5 = Node(5)

node_1.next = node_2
node_2.next = node_3
node_3.next = node_4
node_4.next = node_5

print(find_middle(node_1).key)
