arr = [1,2,2,6,6,6,6,7,10]
class Solution(object):
    def findSpecialInteger(self, arr):
        b = sorted(arr)
        for i in b:
            x = arr.count(i)
            if x > len(arr)*0.25:
                y=i
        return y