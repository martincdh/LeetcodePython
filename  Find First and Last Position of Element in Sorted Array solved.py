class Solution(object):
    def searchRange(self, nums, target):

        if target not in nums:
            return [-1,-1]
        else:
            if nums.count(target) ==1:
                return [nums.index(target), nums.index(target)]
            else:
                for i in range(len(nums)):
                    if nums[i] == target:
                        x = i
                        break
                for j in range(1,len(nums)+1):
                    if nums[-j] == target:
                        y = j 
                        break
                y1 = len(nums) - y
                return [x,y1]