class Solution(object):
    def findDelayedArrivalTime(self, arrivalTime, delayedTime):
        x = arrivalTime + delayedTime
        if x == 24:
            return 0
        elif x > 24:
            while x >24:
                x -=24
            return x
        else:
            return x