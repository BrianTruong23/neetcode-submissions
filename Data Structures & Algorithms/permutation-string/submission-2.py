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

        # get the frequency of each character in s1 and store in a dictionary
        count_s1 = [0] * 26

        def get_index(char):
            return ord(char) - ord('a')

        for s in s1:
            count_s1[get_index(s)] += 1 
    
        # get the frequency of each character in window size of s2 and store in a dictionary 
        count_window_size = [0] * 26
        left = 0 
        right = 0 

        # store the first window size of len s1 of s2 in the dictionary 
        while right < len(s1):
            count_window_size[get_index(s2[right])] += 1 
            right += 1 

        if count_window_size == count_s1:
            return True 

        while right < len(s2):
            count_window_size[get_index(s2[right])] += 1
            count_window_size[get_index(s2[left])] -= 1
            left += 1 

            if count_window_size == count_s1:
                return True 

            right += 1 
        
        return False 





