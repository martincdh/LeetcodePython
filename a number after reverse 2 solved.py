class Solution(object):
    def isSameAfterReversals(self, num):
        num = str(num)
        m = 10
        d = 0 
        a = 0
        for i in range(1, len(num)+1):
            d = d*m + int(num[-i])
        d = str(d)
        for j in range(1, len(d)+1):
            a = a*m + int(d[-j])
        if a == int(num):
            return True
        else:
            return False
        
Input: num = 526
Output: true
Explanation: Reverse num to get 625, then reverse 625 to get 526, which equals num.