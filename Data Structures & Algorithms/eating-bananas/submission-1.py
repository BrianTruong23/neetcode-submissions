class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # calculate the minimum eating speed based on the number of bananas in the pile and the target h hours within
        # the ceiling is the maximum number of bananas in the pile
        # the lowest amount is 1
        # so this is the binary search over finding the eating speed between 1 and the maximum number of bananas in the pile 
        # example: 1, 4, 3, and 2 and h = 9
        # 4 => 4 
        # 1 => sum(banana piles) = 10 
        # 1 => 10 hours, 4 => 4 hours 
        # 4 and 10 

        # naive approach: increase the numbers until it is less than h
        # => example for 1 is 10
        # for 2 is 6 so the answer is 6. 

        # search the eating rate binary 

        def eatingRateToHours(rate):

            if rate == max(piles):
                return len(piles)
            if rate == 1:
                return sum(piles)
            
            hours = 0
            for n in piles:
                hours += n // rate

                if n % rate != 0:
                    hours += 1
            return hours
              

        lo, hi = 1, max(piles)
        mid = (lo + hi) // 2 

        while lo < hi:
            print(lo, hi, mid, eatingRateToHours(mid) )
            if h >=  eatingRateToHours(mid):
                hi = mid 
            else:
                lo = mid + 1 
            mid = (lo + hi) // 2 
        
        return lo 
