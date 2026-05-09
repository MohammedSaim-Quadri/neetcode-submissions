class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_Heap = []
        for x, y in points:
            dist = (x**2) + (y**2)
            heapq.heappush(max_Heap, (-dist, [x,y]))

            if len(max_Heap)>k:
                heapq.heappop(max_Heap)

        return [pair[1] for pair in max_Heap]
        