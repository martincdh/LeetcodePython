class Solution(object):
    def uniqueOccurrences(self, arr):
        b = list(set(arr))
        c =True
        for i in range(len(b)):
            for j in range(i+1, len(b)):
                if arr.count(b[i]) == arr.count(b[j]):
                    c = False
                    break
        return c

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        c = collections.Counter(arr)
        return len(c) == len(set(c.values())) 
    
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.