class Solution(object):
    def addToArrayForm(self, num, k):
        m = 0
        for i in num:
            m = m*10 + i
        m += k
        a = [int(i) for i in str(m)]
        return a

Input: num = [1,2,0,0], k = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234