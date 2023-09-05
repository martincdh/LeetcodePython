class Solution(object):
    def dominantIndex(self, nums):
        x = max(nums)
        index = nums.index(x)
        for i in nums:
            if x < i*2 and x!=i:
                x =-1
        if x != -1:
            return index
        else:
            return -1