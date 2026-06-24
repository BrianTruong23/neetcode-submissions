class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # naive solution: two loops => O(n^2) 
        # better solution: one loop: sliding window technique (O(n))
        # sliding window of size s1 to check s2 
        # if the len of s1 is larger than s2 then we return false 

        # we use an array of size len of s1 
        # count of all the frequency of characters in s1
        # we check the window size of len s1 in s2 and then we compare with each other to see
        # if the dictionary of frequency of s1 is equal to that window size 
        # if it is equal return true 
        # if it is not equal, we move forward from the right pointer and decrease from the left while we update the dictionary 

        if len(s1) > len(s2):
            return False 

        window = [0] * 26
        count_s1 = [0] * 26 

        for s in s1:
            index = ord(s) - ord('a')
            count_s1[index] += 1 

        left = 0 

        for right in range(len(s2)):
        
            window[ord(s2[right]) - ord('a')] += 1 
            if (right - left + 1) > len(s1):
                # decrement left 
                window[ord(s2[left]) - ord('a')] -= 1 
                left += 1 

            # compare two array 
            if window == count_s1:
                return True 
        
        return False


