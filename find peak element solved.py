class Solution(object):
    def findPeakElement(self, nums):
        max_s = nums[0]
        for i in range(len(nums)):
            if nums[i] > max_s:
                max_s = nums[i]
        return nums.index(max_s)

#sol
#snew nums = sort - reverse True- max in index 0 
#return nums.index(newnum)


Input: nums = [1,2,3,1]
Output: 2