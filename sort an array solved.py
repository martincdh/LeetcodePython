class Solution(object):
    def sortArray(self, nums):
        x = sorted(nums)
        return x


Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are 
not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).