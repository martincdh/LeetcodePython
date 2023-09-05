#0,1,1,2,3,5,8,13,21,34,55,89
#-1,0,1,
class Solution(object):
    def fib(self, n):
        
        d=[]
        for j in range(n):
            d.append(j)
        for i in range(len(d)):
            if i in (0,1):
                continue
            else:
                d[i] = d[i-1] +d[i-2]
        if n ==0:
            return 0
        elif n==1:
            return 1
        else:
            return sum([d[-1],d[-2]])
        
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 0
        
        nums=[0]*(n + 1)
        nums[1] += 1

        for i in range(2, len(nums)):
            nums[i] = nums[i-1] + nums[i-2]

        return nums[n]

class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        f0 = 0
        f1 = 1
        f = 0
        if n == 0:
            return f0
        elif n == 1:
            return f1
        f = self.fib(n-1) + self.fib(n-2)
        return f

class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n == 0:
        #     return 0

        # f = [0] * (n + 1)
        # f[1] = 1
        # for i in range(2, n + 1):
        #     f[i] = f[i - 1] + f[i - 2]

        # return f[n]
        def f(n):
            if n == 0 or n == 1:
                return n

            return f(n-1) + f(n-2)

        return f(n)
    
class Solution(object):
    def fib(self, n):
        if n == 0:
            return 0
        a = 0 #=0
        b = 1#1
        c = a + b#1
        for i in range(3, n+1):  # a = 1, b = 1, c = 1 + 1 = 2
            a = b #1
            b = c #1
            c = a + b #2
        return c