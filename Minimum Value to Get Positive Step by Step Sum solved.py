class Solution(object):
    def minStartValue(self, nums):
        i = 0
        x=0
        for j in nums:
            if i+j >1:
                i+=j
            else:

                while i+j< 1:
                    x+=1
                    i+=1
                i+=j

        if x==0:
            return 1
        else:
            return x