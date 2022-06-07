class Solution(object):
    def twoSum(self, nums, target):
      buffer_dictionary = {}
      for i in range(len(nums)):
        if nums[i] in buffer_dictionary:
          return [buffer_dictionary[nums[i]], i] 
        else:
          buffer_dictionary[target - nums[i]] = i 