class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        dict = {}
        for word in strs:
          lcount = [0]*26
          for l in word:
            lcount[ord(l)-ord('a')] += 1
                                    
          wordKey = str(lcount)
          if wordKey in dict:
            dict[wordKey].append(word)            
          else:
            dict[wordKey] = [word]
          
        res = []
        for keys in dict:
          res.append(dict[keys])
          
        return res