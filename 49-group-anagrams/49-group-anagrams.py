class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        
        
        
        """
        
        
        map = {}
        
        for s in strs:
          counter = [0 for i in range(26)]
          for l in s:
            counter[ord(l) - ord("a")] += 1
          counter = tuple(counter)
          if counter not in map:
            map[counter] = []
          map[counter].append(s)
        
        
        return map.values()
          
          
        