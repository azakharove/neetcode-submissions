class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 0:
            return 0
        if len(stones) == 1:
            return stones[0]
        max_heap = [-weight for weight in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            x = -heapq.heappop(max_heap)
            y = -heapq.heappop(max_heap)
            if x == y:
                continue
            if x < y:
                heapq.heappush(max_heap, -(y-x))
            if y < x:
                heapq.heappush(max_heap, -(x-y))
        if len(max_heap) == 0:
            return 0
        if len(max_heap) == 1:
            return -max_heap[0]
        