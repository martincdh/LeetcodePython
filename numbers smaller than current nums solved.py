class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        d = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[i] > nums[j] and i !=j:
                    count+=1
            d.append(count)
        return d

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]

Input: nums = [6,5,4,8]
Output: [2,1,0,3]