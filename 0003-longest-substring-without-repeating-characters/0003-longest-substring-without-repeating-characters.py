class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        count = set()
        L, res = 0, 1


        # abcabcbb
        #    ^
        #  ^

        for R in range(len(s)):   
            while s[R] in count:
                count.remove(s[L])
                L += 1
            count.add(s[R])
            res = max(res, R-L+1)
        
        return res
        

