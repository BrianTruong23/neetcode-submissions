import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        
# add to the heap 
# pop two each time 
# push or destroy both  
# implement with max heap 
        heap = []
        for i in stones:
            heapq.heappush(heap, -i)
        
        while len(heap) > 1:
            first = -(heapq.heappop(heap))
            second = -(heapq.heappop(heap))

            if first > second:
                heapq.heappush(heap, - (first - second))
            elif second > first:
                heapq.heappush(heap, - (second - first))
        
        if len(heap) == 0:
            return 0 
        
        return -heap[0]


        