class Solution(object):
    def targetIndices(self, nums, target):
        nums = sorted(nums)
        d =[]
        for i in range(len(nums)):
            if nums[i] == target:
                d.append(i)
        return d