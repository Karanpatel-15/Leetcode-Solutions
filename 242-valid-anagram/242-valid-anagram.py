class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        sDict = {}
        tDict = {}

        for l in s:
            if l not in sDict:
                sDict[l] = 1
            else:
                sDict[l] += 1
        
        for l in t:
            if l not in tDict:
                tDict[l] = 1
            else:
                tDict[l] += 1
                
        if len(sDict) != len(tDict):
            return False
        else:
            for l in sDict:
                if l not in tDict or sDict[l] != tDict[l]:
                    return False
                
        return True
                
        