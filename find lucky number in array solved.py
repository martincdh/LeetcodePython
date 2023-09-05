arr = [2,2,3,4]
arr = [1,2,2,3,3,3]
arr = [2,2,2,3,3]
m = list(set(arr))
class Solution(object):
    def findLucky(self, arr):
        m = list(set(arr))
        max_s = 0
        for i in m:
            if i == arr.count(i) and i>max_s:
                max_s = i
        if max_s != 0:
            return max_s
        else:
            return -1
