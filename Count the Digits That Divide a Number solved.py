class Solution(object):
    def countDigits(self, num):
        a = str(num)
        count = 0
        for i in range(len(a)):
            if num % int(a[i]) ==0:
                count+=1
        return count