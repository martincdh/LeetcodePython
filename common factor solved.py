class Solution(object):
    def commonFactors(self, a, b):
        count = 0
        if a > b:
            for i in range(1,a+1):
                if a%i ==0 and b%i == 0:
                    count+=1
        else:
            for i in range(1,b+1):
                if a%i ==0 and b%i == 0:
                    count+=1
        return count

Input: a = 12, b = 6
Output: 4
Explanation: The common factors of 12 and 6 are 1, 2, 3, 6.