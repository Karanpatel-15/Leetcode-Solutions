class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSum = []
        total = 0
        for n in nums:
            total += n
            self.prefixSum.append(total)
            
        

    def sumRange(self, left: int, right: int) -> int:
        preR = self.prefixSum[right]
        preL = self.prefixSum[left-1] if left != 0 else 0
        return preR-preL
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)