from collections import Counter
import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        
        """
        
        counter = Counter(nums)
        
        bucket = [[] for i in range(len(nums)+1)]
        
        for key in counter:
          bucket[counter[key]].append(key)
          
        res = []
        for i in range(len(bucket)-1, 0, -1):
          if bucket[i] == []:
            continue
            
          for j in bucket[i]:
            if k == 0:
              return res
            res.append(j)
            k-=1
            
        return res
          
          
        
        
        
        # heap = []
#         for key in counter:
#           t = (-counter[key], key)
#           heapq.heappush(heap, t)
          
#         res = []
#         for i in range(k):
#           res.append(heapq.heappop(heap)[1])
          
#         return res
        
        
        