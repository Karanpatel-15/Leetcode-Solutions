from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        s1 = Counter(ransomNote)
        s2 = Counter(magazine)
        
        
        for l in s1:
          if l not in s2 or s2[l] < s1[l]:
            return False
          
        return True