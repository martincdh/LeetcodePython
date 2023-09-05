class Solution(object):
    def kItemsWithMaximumSum(self, numOnes, numZeros, numNegOnes, k):
        if numOnes >= k:
            return k
        elif numOnes <k:
            x = k -numOnes
            if numZeros >= x:
                return numOnes
            else:
                return numOnes+(x-numZeros)*-1

