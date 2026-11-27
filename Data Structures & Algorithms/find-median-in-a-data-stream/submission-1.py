from heapq import heapify, heappush, heappop
class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        heapify(self.min_heap)
        heapify(self.max_heap)
        self.l_min_heap = 0
        self.l_max_heap = 0

    def addNum(self, num: int) -> None:
        if self.min_heap and self.min_heap[0] < num:
            heappush(self.min_heap, num)
            self.l_min_heap += 1

            # check for rebalancing
            if self.l_min_heap - self.l_max_heap > 1:
                ele = heappop(self.min_heap)
                heappush(self.max_heap, -ele)
                self.l_min_heap -= 1
                self.l_max_heap += 1

        else:
            heappush(self.max_heap, -num)
            self.l_max_heap += 1
        
            # check for rebalancing
            if self.l_max_heap - self.l_min_heap > 1:
                ele = -heappop(self.max_heap)
                heappush(self.min_heap, ele)
                self.l_max_heap -= 1
                self.l_min_heap += 1
            
        # print(self.max_heap, self.min_heap)

    def findMedian(self) -> float:
        if self.l_min_heap - self.l_max_heap == 1:
            return self.min_heap[0]
        elif self.l_max_heap - self.l_min_heap == 1:
            return -self.max_heap[0]
        else:
            return (self.min_heap[0] - self.max_heap[0])/2
