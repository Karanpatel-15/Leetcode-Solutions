class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        count = {}
        for l in s:
          count[l] = count.get(l, 0) + 1
          
        maxHeap = []
        for l in count:
          maxHeap.append([-count[l], l])
          
        heapq.heapify(maxHeap)
        
        prev = None
        res = ""
        while maxHeap or prev:
          if prev and not maxHeap:
            return ""
          
          count, letter = heapq.heappop(maxHeap)
          res += letter
          count += 1
          
          if prev:
            heapq.heappush(maxHeap, prev)
            
          prev = None
          if count != 0:
            prev = [count, letter]
            
        return res
          
            