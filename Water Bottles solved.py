class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        x = numBottles - (numBottles//numExchange)*numExchange + numBottles//numExchange

        total = numBottles + numBottles//numExchange
        while x >= numExchange:
            total += x//numExchange
            x = x-(x//numExchange)*numExchange + x//numExchange
        return total

Input: numBottles = 9, numExchange = 3
Output: 13
Explanation: You can exchange 3 empty bottles to get 1 full water bottle.
Number of water bottles you can drink: 9 + 3 + 1 = 13.

Input: numBottles = 15, numExchange = 4
Output: 19
Explanation: You can exchange 4 empty bottles to get 1 full water bottle. 
Number of water bottles you can drink: 15 + 3 + 1 = 19.

