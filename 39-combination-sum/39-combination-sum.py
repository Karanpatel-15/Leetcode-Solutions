class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        res = []
        
        
        def dfs(total, curr, i):
          if total == target:
            res.append(curr[:])
            return
          elif i == len(candidates) or total > target:
            return
          
          dfs(total+candidates[i], curr+[candidates[i]], i)
          dfs(total, curr, i+1)
            
          return
        
        dfs(0, [], 0)
        
        return res        