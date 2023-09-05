class Solution(object):
    def singleNumber(self, nums):
        x = list(set(nums))
        for i in x:
            if nums.count(i) ==1:
                return i
                break


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                i += 3
            else:
                return nums[i]
        return nums[len(nums)-1]
    

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = defaultdict(int)
        for i in range(len(nums)):
            d[nums[i]] += 1
        for key, value in d.items():
            if value == 1:
                return key
            
Input: nums = [0,1,0,1,0,1,99]
Output: 99