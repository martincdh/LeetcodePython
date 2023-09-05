class Solution(object):
    def accountBalanceAfterPurchase(self, purchaseAmount):
        if purchaseAmount %10 !=0:    
            count1 = 0
            count2 = 0
            a=b=purchaseAmount
            while a %10 != 0:
                a+=1
                count1+=1

            while b%10 !=0:
                b-=1
                count2+=1
            if count1 > count2:
                return 100 - b
            else:
                return 100-a
            

            return 100 - purchaseAmount
        else:
            return 100 - purchaseAmount
    
purchaseAmount = 9
