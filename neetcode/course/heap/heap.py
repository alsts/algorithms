class MinHeap:
    def __init__(self):
        self.heap = [0]  # Skip first element

    def push(self, val):
        self.heap.append(val)  # Simply append node to the end of array
        i = len(self.heap) - 1  # Assign Current node pointer to New node - Last in Array

        # Percolate up - (move current up if lower than parents)
        while self.heap[i] < self.heap[i // 2]:
            # Current node is lower than Parent node -> swap Current with Parent -> move Up
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i = i // 2

    def pop(self):
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()

        min_item = self.heap[1]
        self.heap[1] = self.heap.pop()  # Move last item to the root
        self.percolate_down(1)  # Percolate down -> move current down until any of children is lower
        return min_item

    def heapify(self, arr):
        # 0th position is moved to the end
        arr.append(arr[0])

        self.heap = arr
        cur = (len(self.heap) - 1) // 2  # Can safely skip half of array -> no children
        while cur > 0:
            self.percolate_down(cur)  # Percolate down -> move current down until any of children is lower
            cur -= 1

    def percolate_down(self, i):
        while 2 * i < len(self.heap):  # loop until have left child (not leaf)
            if self.currentHasRightChild(i) and self.rightChildLowerThanLeft(i) and self.rightChildLowerThanCurrent(i):
                # Swap Current with Right child - move current node Down
                self.heap[2 * i + 1], self.heap[i] = self.heap[i], self.heap[2 * i + 1]
                i = 2 * i + 1
            elif self.leftChildLowerThanCurrent(i):
                # Swap Current with Left child - move current node Down
                self.heap[2 * i], self.heap[i] = self.heap[i], self.heap[2 * i]
                i = 2 * i
            else:
                # Current node is lower than its children
                break

    def currentHasRightChild(self, i):
        return 2 * i + 1 < len(self.heap)

    def rightChildLowerThanLeft(self, i):  # In heap if has right -> must have left child!!!
        return self.heap[2 * i + 1] < self.heap[2 * i]

    def rightChildLowerThanCurrent(self, i):
        return self.heap[2 * i + 1] < self.heap[i]

    def leftChildLowerThanCurrent(self, i):
        return self.heap[2 * i + 1] < self.heap[i]


if __name__ == "__main__":
    minHeap = MinHeap()
    minHeap.push(15)
    minHeap.push(5)
    minHeap.push(3)
    minHeap.push(17)
    minHeap.push(10)
    minHeap.push(84)
    minHeap.push(19)
    minHeap.push(6)
    minHeap.push(22)
    minHeap.push(9)

    print(minHeap.pop())
    print(minHeap.pop())
    print(minHeap.pop())
    print(minHeap.pop())
    print(minHeap.pop())
    print(minHeap.pop())
    print(minHeap.pop())
