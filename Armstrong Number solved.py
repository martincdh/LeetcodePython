class Solution(object):
    def isArmstrong(self, n):
        n = str(n)
        x = len(n)
        m = 0
        for i in range(len(n)):
            m += pow(int(n[i]),x)
        if m == int(n):
            return True
        else:
            return False 