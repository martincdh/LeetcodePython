class Solution(object):
    def arraySign(self, nums):
        d=1
        for i in nums:
            d*=i
        if d>=1:
            return 1
        elif d == 0:
            return 0
        else:
            return -1