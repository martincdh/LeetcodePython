class Solution(object):
    def selfDividingNumbers(self, left, right):
        d =[]
       
        for i in range(left, right+1):
            count = 0
            i =str(i)
            print(i)
            if '0' not in i:
                for j in range(len(i)):
                    if int(i) % int(i[j]) ==0:
                        count+=1
            if count == len(str(i)):
                d+= [int(i)]
        return d
Input: left = 1, right = 22
Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]