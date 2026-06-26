import heapq
from collections import deque 
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        

        # sliding window of size k and we slide to the right 
        # we move to the right one position at each time and then we record the max
        
        # max heap to store the max value at the top to retrieve 
        # we store the number and the index value 
        # then we keep track of left and when the value is old (its index is less than left), we remove that from the heap 

        dq = deque()
        max_result = []
        left = 0 

        for right in range(len(nums)):

            # append to the back 
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()
                # pop from the back whenever the value of nums[right] is larger to the value in the back because the nums[right] is the latest value and larger value than any of this here

            dq.append(right)

            if dq and dq[0] < left:
                dq.popleft()

            if right >= k - 1:
                # we append the max to the max result 
                max_result.append(nums[dq[0]])
                left += 1 
                

        return max_result













# use double ended deque: O(n)
    # it appends the indices to both the front and the back
    # the front: index of the current maximum
    # the back: index of the values that might become maximum later 
    # keep values that indices point to as: front: current maximum and back: values that might become maximum later 
# Naive uses O(n * k) 
# Heap uses O(nlogn)
        # heap = [] 
        # max_result = []
        
        # left = 0 
        # for right in range(len(nums)):
            
        #     # push to the heap 
        #     # O(1)
        #     heapq.heappush(heap, (-nums[right], right))

        #     # when the number is equal or larger than k - 1, we append to the result 
        #     if right >= (k - 1):
        #         # print("nums[right]: ", nums[right])
        #         # print("heap before", heap)
        #         max_result.append(-heap[0][0])

        #         # we move left up 
        #         left += 1 

        #         # we peak at the current max index 
        #         while heap and (heap[0][1]) < left:
        #             # if it is old, we remove it 
        #             # O(1)
        #             heapq.heappop(heap)
                
        #         # print("heap after", heap)
            
        
        # return max_result









