class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        else:
            while(n%3==0):
                n=n/3
            return n==1
        
class Solution(object):
    def isPowerOfThree(self, n):
        for i in range(0,100):
            if 3**i == n:
                return True
        """
        :type n: int
        :rtype: bool
        """