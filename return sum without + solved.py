class Solution(object):
    def getSum(self, a, b):
        if a == 0 and b != 0:
            return b
        elif b ==0 and a !=0:
            return a
        
        return int(log(exp(a) * exp(b)))
        
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        return sum([a,b])
    
print(sum([1,2]))