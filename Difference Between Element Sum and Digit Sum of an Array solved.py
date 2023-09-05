
nums = [1,8,5,6,4,8,4,1,9,10]
sum1 = 0
count = 0
sum2 = 0

for i in nums:
    sum1 +=i
    count = count*10 +i
b = str(count)
for j in range(len(b)):
    sum2 += int(b[j])

print(sum1)
print(sum2)
print(count)
print(sum1 - sum2)

##final sol

class Solution(object):
    def differenceOfSum(self, nums):
        sum1 = 0
        count = ""
        sum2 = 0

        for i in nums:
            sum1 +=i
            count += str(i)
        
        for j in range(len(count)):
            sum2 += int(count[j])

        return abs(sum1 - sum2)
