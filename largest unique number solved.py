class Solution(object):
    def largestUniqueNumber(self, nums):
        a = -1
        x = list(set(nums))
        x = sorted(x)
        for i in range(1,len(x)+1):
            if nums.count(x[-i]) == 1:
                a = x[-i]
                break
        return a

