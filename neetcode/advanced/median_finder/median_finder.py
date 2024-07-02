import heapq


class MedianFinder:
    def __init__(self):
        self.small, self.large = [], []

    def insert(self, num: int) -> None:
        # Push to the small Heap(MaxHeap)
        heapq.heappush(self.small, -1 * num)

        # Check if small_heap(max) is <= large_heap(min) -> if not swap
        if self.small and self.large and (-1 * self.small[0]) > self.large[0]:
            small_heap_max = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, small_heap_max)

        # Check if heaps are balanced
        if len(self.small) > len(self.large) + 1:
            # Small heap size larger by 2 elements -> move max to Large Heap
            small_heap_max = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, small_heap_max)
        if len(self.large) > len(self.small) + 1:
            # Large heap size larger by 2 elements -> move min to Small Heap
            large_heap_min = heapq.heappop(self.large)
            heapq.heappush(self.small, large_heap_min)

    def get_median(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]

        # Even number of elements in Heaps, return avg of two middle nums
        return ((-1 * self.small[0]) + self.large[0]) / 2


median_finder = MedianFinder()
median_finder.insert(4)
print(median_finder.get_median())

median_finder.insert(7)
print(median_finder.get_median())

median_finder.insert(3)
print(median_finder.get_median())

median_finder.insert(5)
print(median_finder.get_median())

median_finder.insert(1)
print(median_finder.get_median())
