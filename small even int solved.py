class Solution(object):
    def smallestEvenMultiple(self, n):
        if n%2 ==0:
            return n
        else:
            return 2*n

Input: n = 5
Output: 10
Explanation: The smallest multiple of both 5 and 2 is 10.