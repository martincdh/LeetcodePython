class Solution(object):
    def threeConsecutiveOdds(self, arr):
        x = False
        if len(arr) <3:
            return x
        else:
            for i in range(len(arr)):
                if i == len(arr)-1:
                    break
                elif i < len(arr) -2 and arr[i] %2 !=0 and arr[i+1] %2 !=0 and arr[i+2] %2 !=0:
                    x = True
            return x


class Solution(object):
    def threeConsecutiveOdds(self, arr):
        for u in range(len(arr)-2):
            if arr[u]%2!=0 and arr[u+1]%2!=0 and arr[u+2]%2!=0:
                return True
        return False

class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        for i in range(1, len(arr) - 1):
            if arr[i - 1] % 2 != 0 and arr[i] % 2 != 0 and arr[i + 1] % 2 != 0:
                return True
        return False

class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        if len(arr) < 3:
            return False

        for i in range(2,len(arr)):
            if arr[i]%2 != 0 and arr[i-1]%2 != 0 and arr[i-2]%2 != 0:
                return True
        return False