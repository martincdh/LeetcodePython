class Solution(object):
    def isMajorityElement(self, nums, target):
        x = len(nums) /2
        y = nums.count(target)
        if y>x:
            return True
        else:
            return False
        

Input: nums = [2,4,5,5,5,5,5,6,6], target = 5