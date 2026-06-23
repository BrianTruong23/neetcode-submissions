class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # sliding window
        # keep track of a character that is not the same 
        # keep track of the frequency of the characters in a hashmap
        # 
        # naive solution: consider all substrings and use hashmap for freqency 
        # better solution: using sliding window to consider 
        # AAABAAABBBB, k = 3 

        # add to the hashmap the right characters  
        # update max_count = max(count[s[right]], max_count)
        # deteremine replacements 
        # if replacement <= k, valid => update best 
        # if it is not valid, update left += 1, decrement the count for s[left]: count[s[left]] -= 1 

        # there is a maxcount that is stale when we go from left to right, however it does not change the output because we have earlier window with that same max count to support it 
        # it may delay shrinking but not change the final output. 

        left = 0
        best = 0
        max_count = 0
        count = {}

        for right in range(len(s)):

            print("s[right]", s[right])

            if s[right] in count:
                count[s[right]] += 1
            else:
                count[s[right]] = 1 

            max_count = max(max_count, count[s[right]])
            length = right - left + 1 
            replacement = length - max_count 

            print("max_count", max_count, "replacement", replacement)
            print(count)

            if replacement <= k:
                best = max(best, length)
            else:
                count[s[left]] -= 1 
                left += 1 
        
        return best 