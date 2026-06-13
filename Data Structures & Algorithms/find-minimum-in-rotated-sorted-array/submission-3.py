class Solution:
    def findMin(self, nums: List[int]) -> int:
        # i know binary search works in this problem 
        # just need to know where the minimum located in a list of rotated array 
        # there is no typical target but we can replace the target with lo and hi so that we can compare that to the sequence
        # we can have a value to keep track of min 

        # min will be initialized as largest value first 
        # min = largest int 
        # if nums[mid] < min => update min 
        # return min 

        # if mid < hi: get the min => go to the left 
        # if mid > lo: get the min => go to the right 
        # repeat while lo <= hi 

        lo, hi = 0, len(nums) - 1
        min_ = 1001
        
        # time = 0 
        while lo <= hi:
            mid = (lo + hi) // 2 

            if nums[mid] < min_:
                min_ = nums[mid]
            
            if nums[lo] <= nums[mid]:
                # increasing order sequence on the left 
                # capture min 
                if nums[lo] < min_:
                    min_ = nums[lo]
                # go to the right 
                lo = mid + 1 
            else:
                # already captured the min because it is mid 
                # go to the left 
                hi = mid - 1
            
        return min_

