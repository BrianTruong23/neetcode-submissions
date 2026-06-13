class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # need to access lo, hi
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2 
            print(lo, mid, hi)

            if target == nums[mid]:
                return mid 

            if nums[mid] <= nums[hi]:
                # right side is sorted 
                if (nums[mid] < target <= nums[hi]):
                    # go to the right 
                    lo = mid + 1 
                else:
                    # go to left 
                    hi = mid - 1
            else:
                # left side is sorted 
                if (nums[mid] > target >= nums[lo]):
                    # go to the left 
                    hi = mid - 1 
                else:
                    # go to the right 
                    lo = mid + 1
            
        return -1 