class Solution(object):
    def canBeEqual(self, target, arr):
        target = sorted(target)
        arr =sorted(arr)
        if target == arr:
            return True
        else:
            return False

Input: target = [1,2,3,4], arr = [2,4,1,3]
Output: true

Input: target = [3,7,9], arr = [3,7,11]