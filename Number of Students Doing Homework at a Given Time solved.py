class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        count = 0
        for i in range(len(startTime)):
            for j in range(len(endTime)):
                if i == j and queryTime in range(startTime[i], endTime[j]+1):
                    count+=1
        return count
    
Input: startTime = [4], endTime = [4], queryTime = 4

Input: startTime = [1,2,3], endTime = [3,2,7], queryTime = 4
Output: 1