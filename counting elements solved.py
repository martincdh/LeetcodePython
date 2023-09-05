class Solution(object):
    def countElements(self, arr):
        count = 0
        for i in arr:
            if i +1 in arr:
                count+=1
        return count
    
Input: arr = [1,2,3]
Output: 2
Explanation: 1 and 2 are counted cause 2 and 3 are in arr.