class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        L, R = 0,0
        curSum = nums[0]
        res = 0

        # [2,3,1,2,4,3]
        #        ^
        #    ^

        while True:
            if curSum >= target:
                if res == 0:
                    res = R-L+1
                else:
                    res = min(res, R-L+1)
                curSum -= nums[L]
                L += 1
            else:
                R += 1
                if R == len(nums):
                    break
                curSum += nums[R]

        return res

            

        