import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        

        # sliding window of size k and we slide to the right 
        # we move to the right one position at each time and then we record the max
        
        # max heap to store the max value at the top to retrieve 
        # we store the number and the index value 
        # then we keep track of left and when the value is old (its index is less than left), we remove that from the heap 

        heap = [] 
        max_result = []
        
        left = 0 
        for right in range(len(nums)):
            
            # push to the heap 
            heapq.heappush(heap, (-nums[right], right))

            # when the number is equal or larger than k - 1, we append to the result 
            if right >= (k - 1):
                # print("nums[right]: ", nums[right])
                # print("heap before", heap)
                max_result.append(-heap[0][0])

                # we move left up 
                left += 1 

                # we peak at the current max index 
                while heap and (heap[0][1]) < left:
                    # if it is old, we remove it 
                    heapq.heappop(heap)
                
                # print("heap after", heap)
            
        
        return max_result









