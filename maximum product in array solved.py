class Solution(object):
    def maxProduct(self, nums):
        max_s = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i]-1)*(nums[j]-1) > max_s:
                    max_s = (nums[i]-1)*(nums[j]-1)
        return max_s
    
Input: nums = [3,4,5,2]
Output: 12 

Input: nums = [1,5,4,5]
Output: 16