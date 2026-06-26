class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        

        # sliding window of size k and we slide to the right 
        # we move to the right one position at each time and then we record the max

        if k > len(nums):
            return max(nums)

        max_list = []

        max_list.append(max(nums[0:k]))

        for right in range(k, len(nums)):

            leftmost = right - k + 1

            # print(nums[leftmost:right+1])

            max_list.append(max(nums[leftmost:right+1]))

        return max_list

