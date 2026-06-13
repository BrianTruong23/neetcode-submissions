class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # right means that the target is larger than mid and lo
            # or the target is smaller than both mid and lo 
        # left means that the target is smaller than mid and larger than lo 

        # case of 1 
        if len(nums) == 1 & target == nums[0]:
            return 0
        
        # need to access lo, hi
        lo, hi = 0, len(nums) - 1

        while lo < hi:
            mid = (lo + hi) // 2 
            # print(lo, mid, hi)

            if target == nums[mid]:
                return mid 
            if target == nums[lo]:
                return lo
            if target == nums[hi]:
                return hi 

            if (nums[mid] > nums[lo]):
                # the increasing sequence on the left 
                if (target) < nums[mid] and target > nums[lo]:
                    # go the left
                    hi = mid 
                else: 
                    # go the right 
                    lo = mid + 1 
            elif (nums[mid] < nums[hi]):
                # the increasing sequence on the right 
                if (target < nums[hi] and target > nums[mid]):
                    # go to the right 
                    lo = mid + 1
                else:
                    hi = mid
            else:
                # on either side so we just decrease in either side 
                lo += 1
                hi -= 1 

        return -1

    # 5, 1 , 2
