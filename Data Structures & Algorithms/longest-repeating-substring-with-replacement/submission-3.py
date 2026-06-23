class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # sliding window
        # keep track of a character that is not the same 
        # keep track of the frequency of the characters in a hashmap
        # 
        # naive solution: consider all substrings and use hashmap for freqency 
        # better solution: using sliding window to consider 
        # AAABAAABBBB, k = 3 

        # for a given window
            # when we add to the right
                # add the frequency to the hashed map 
                # get the replacement by window length - most frequent characters in the window 
                # compare replacement with k
                # if it is valid continue (compare the maximum with the current max)
                # if it is not valid (then we move left forward and decrement the count)
            
        left = 0
        count = {}
        best = 0
        max_count = 0

        for right in range(len(s)):
            
            print("s[right]: ", s[right])
            if s[right] in count:
                count[s[right]] += 1
            else:
                count[s[right]] = 1
            print("count:", count)
            length = right - left + 1
            max_count = max(max_count, count[s[right]])
            # replacement needed 
            replacement_needed = (length) - max_count 
            print("replacement: ", replacement_needed)
            if replacement_needed <= k:
                # still valid 
                # update max_count, best 
                
                best = max(best, length)
                print("best: ", best, " max_count: ", max_count)

            else:
                # not valid anymore 
                count[s[left]] -= 1 
                left += 1 
        return best 

        
# AAABABBBB

# A:1
# A: 2
# A: 3
# A: 3, B: 1
# A:4, B = 1 
# B: 2, 

            
            



        