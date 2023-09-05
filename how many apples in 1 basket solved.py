

weight = [100,200,150,1000,2000,10,11,4000]
class Solution(object):
    def maxNumberOfApples(self, weight):
        weight = sorted(weight)
        m = 0
        for i in range(len(weight)):
            m+= weight[i]
            if m >5000:
                return i
                break
            elif i == len(weight) -1 and m <=5000:
                return i+1



