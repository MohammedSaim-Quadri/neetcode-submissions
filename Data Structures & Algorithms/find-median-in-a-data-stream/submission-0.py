class MedianFinder:

    def __init__(self):
        self.max_heap=[]
        self.min_heap=[]
        

    def addNum(self, num: int) -> None:
        if not self.max_heap or num<= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        if abs(len(self.max_heap) - len(self.min_heap)) > 1:
            if len(self.max_heap) > len(self.min_heap):
                b = -heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, b)
            if len(self.min_heap) > len(self.max_heap):
                b = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -b)

        

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        elif len(self.max_heap) > len(self.min_heap):
            return float(-self.max_heap[0])
        else:
            return float(self.min_heap[0])
        
        