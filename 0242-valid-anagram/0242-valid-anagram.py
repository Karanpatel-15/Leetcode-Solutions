class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        sMap = {}
        tMap = {}

        for i in range(len(s)):
            if s[i] in sMap:
                sMap[s[i]] += 1
            else:
                sMap[s[i]] = 1

            if t[i] in tMap:
                tMap[t[i]] += 1
            else:
                tMap[t[i]] = 1

        for l in sMap:
            if l not in tMap or tMap[l] != sMap[l]:
                return False
        
        return True


        
