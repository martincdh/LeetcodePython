class Solution(object):
    def findGCD(self, nums):
        a = max(nums)
        b = min(nums)
        m=0
        for i in range(1,a+1):
            if a%i ==0 and b%i==0 and i>m:
                m=i
        return m

Input: nums = [2,5,6,9,10]
Output: 2

Input: nums = [7,5,6,8,3]
Output: 1