import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        buckets = [[] for i in range(len(nums)+1)]
        for num in nums:
          if num in count:
            count[num] += 1
          else:
            count[num] = 1
            
        for key in count:
          buckets[count[key]].append(key)
          
        res = []
        for i in range(len(nums), 0, -1):
          for num in buckets[i]:
            res.append(num)
            if len(res) == k:
              return res
          
        
        
        