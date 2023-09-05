class Solution(object):
    def reverse(self, x):
    
        m = len(str(x))
        
        
        if x >=0:
            x = str(x)
            y= int(x[-1::-1])
        else:
            x = str(x)
            y= int(x[-1:-m:-1]) *-1

        if y >= pow(-2,31) and y<= pow(2,31) -1:
            return y
        else:
            return 0
Input: x = 123
Output: 321