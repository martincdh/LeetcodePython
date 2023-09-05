class Solution(object):
    def isFascinating(self, n):
        x = str(n)
        x += str(n*2) + str(n*3)
        for i in range (1,10):
            if str(i) not in x or x.count(str(i)) > 1:
                return False
        return True
    
Input: n = 192
Output: true

Input: n = 100
Output: false