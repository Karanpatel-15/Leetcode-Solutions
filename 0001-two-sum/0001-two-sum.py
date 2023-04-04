class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        map = {}

        for i in range(len(nums)):
            requiredNum = target - nums[i] 

            if requiredNum in map:
                return [map[requiredNum], i]
            else:
                map[nums[i]] = i