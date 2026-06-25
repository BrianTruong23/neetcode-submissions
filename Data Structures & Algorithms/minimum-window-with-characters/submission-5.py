class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # shortest substring in s from t 
        # all character of t needs to exist in s

        # the substring in s needs to be the shortest that contain all characters in t 
        # different than permutation: we cannot put a fixed size window and slide at every characters of s to compare. 
        
        if s == t:
            return s

        if len(t) > len(s):
            return ""

        count_t = [0] * 52 
        count_window = [0] * 52 

        def get_index(t1):
            if t1.isupper():
                return ord(t1) - ord('A') + 26
            else:
                return ord(t1) - ord('a')
            
        list_index = []

        def return_bool_larger_equal_frequencies(count_t, count_window):
            for index in list_index:
                if count_window[index] < count_t[index]:
                    return False 
            return True
            
        def return_bool_matching_if_decrement(count_t, count_window, left):
            count_window[get_index(s[left])] -= 1 

            if return_bool_larger_equal_frequencies(count_t, count_window):
                return True 
            else:
                count_window[get_index(s[left])] += 1 
                return False 

        def return_bool_at_least_frequencies(count_t, count_window):
            for index in list_index:
                if count_window[index] < count_t[index]:
                    return False 
            return True 

        # get the frequencies and incremeent the frequencies in the array of t1 

        for t1 in t:
            count_t[get_index(t1)] += 1 
            list_index.append(get_index(t1))

        left = 0
        result = f"0{s}{t}"

        for right in range(len(s)):
            count_window[get_index(s[right])] += 1 

            if return_bool_at_least_frequencies(count_t, count_window):
                # print("s[right]", s[right])
                # if the left got decremented and it is still matching then shrink 
                while return_bool_matching_if_decrement(count_t, count_window, left) and left < len(s):
                    # shrink the size of the window if the count_t is in count_window
                    # print("left decremented", s[left])
                    left += 1

                if (right - left + 1) < len(result):
                    result = s[left:right + 1]

        if result == f"0{s}{t}":
            return ""

        return result 



        
        # there are two problem:
            # 1) how to know if the windowsize satisfies the character in t? I think we can use == for this 
            # 2) how to find minimum substring 



        
