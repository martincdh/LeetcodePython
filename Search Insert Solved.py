class Solution(object):
    def searchInsert(self, nums, target):
        if target in nums:
            for i in range(len(nums)):
                if nums[i] == target:
                    return i
        else:
            nums.append(target)
            nums.sort()
            for i in range(len(nums)):
                if nums[i] == target:
                    return i