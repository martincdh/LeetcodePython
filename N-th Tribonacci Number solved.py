

class Solution(object):
    def tribonacci(self, n):
        d=[]
        for j in range(n+1):
                d.append(j) #[0,1,2,3]
        for i in range(len(d)):
                if i in (0,1):
                    continue
                elif i ==2:
                    d[i] =1
                else:
                    d[i] =d[i-3]+d[i-1] +d[i-2] #d[2]= 1+0+2 
        if n ==0:
            return 0
        elif n==1:
            return 1
        else:
            return d[-1]
        
    #The Tribonacci sequence Tn is defined as follows: 

#T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
#Example 1:

#Input: n = 4
#Output: 4
#Explanation:
#T_3 = 0 + 1 + 1 = 2
#T_4 = 1 + 1 + 2 = 4
#Example 2:

#Input: n = 25
#Output: 1389537