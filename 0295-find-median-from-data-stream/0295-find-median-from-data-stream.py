class MedianFinder:

    def __init__(self):
        self.maxheap, self.minheap = [], []

    def addNum(self, num: int) -> None:
        if self.minheap and num > self.minheap[0]:
            heapq.heappush(self.minheap, num)
        else:
            heapq.heappush(self.maxheap, -1*num)
        
        if len(self.maxheap) > len(self.minheap) + 1:
            heapq.heappush(self.minheap, -1 * heapq.heappop(self.maxheap))
        if len(self.minheap) > len(self.maxheap) + 1:
            heapq.heappush(self.maxheap, -1 * heapq.heappop(self.minheap))

    def findMedian(self) -> float:
        if len(self.maxheap) > len(self.minheap):
            return -1 * self.maxheap[0]
        elif len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        else:
            return ((-1 * self.maxheap[0]) + self.minheap[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()