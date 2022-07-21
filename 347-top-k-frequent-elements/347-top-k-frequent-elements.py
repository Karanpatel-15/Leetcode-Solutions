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
        
        heap = []
        
        for key in counter:
          t = (-counter[key], key)
          heapq.heappush(heap, t)
          
        res = []
        for i in range(k):
          res.append(heapq.heappop(heap)[1])
          
        return res
        
        
        