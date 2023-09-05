class Solution(object):
    def getNoZeroIntegers(self, n):
        for i in range(n):
            if '0' in str(i):
                continue
            else:
                for j in range(n):
                    if '0' in str(j):
                        continue
                    else:
                        if i+j == n and i!=0 and j!=0:
                            return [i,j]
                            break


#create a new def function to check i for i in range(n)

class Solution(object):
    def getNoZeroIntegers(self, n):
        def check(num):
            while num>0:
                if num%10==0: #check if divide by 10
                    return False
                num//=10  
            return True
        for i in range(1,n):
            t=n-i
            if check(t) and check(i):
                return [i,t]
