def two(nums, k):
    max_sum1 = 0
    for i in range(len(nums)):
        for j in range( i+1, len(nums)):
            
            if(i<j and nums[i] + nums[j] < k):
                max_sum = nums[i] + nums[j]
                if max_sum >= max_sum1 and i<j:
                    max_sum1 = max_sum
                
    if max_sum1 == 0:
        max_sum1 = -1
    print(max_sum1)
            

def maxProfit(prices):
   
    max_s = 0
    for a in range(len(prices)):
        for b in range(a+1, len(prices)):
            if prices[b] -prices[a] > 0:
                max_sum = prices[b] - prices[a]
                if max_sum >= max_s and a<b:
                    max_s= prices[b] - prices[a]
            
    print(max_s)            
                


two(nums = [10,20,30], k = 15)

maxProfit(prices = [10,9,8,7,5,4])


m = [7,6,4,3,1]
n = max(m)

print(n)

