class Solution(object):
    def numberOfMatches(self, n):
        count = 0
        while n != 1:
            if n%2 ==0:

                count += n//2
                n = n//2
            else:
                count += (n-1)//2
                n = (n-1)//2 +1

        return count
    
class Solution(object):
    def numberOfMatches(self, n):
        return n-1
    
class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        elif n < 2:
            return 0
        matches = n / 2 if n % 2 == 0 else (n-1)/2
        return matches + self.numberOfMatches(n-matches)
    
Input: n = 7
Output: 6

Input: n = 14
Output: 13