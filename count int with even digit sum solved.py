class Solution(object):
    def countEven(self, num):
        count = 0
        for i in range (2,num+1):
            x = sum([int(a) for a in str(i)])
            if x %2 ==0:
                count+=1
        return count
    
def countEven(self, num):
       return num // 2 if sum([int(k) for k in str(num)]) % 2 == 0 else (num - 1) // 2


#sol 2

class Solution(object):
    @staticmethod
    def digitSum(num):
        digit_sum = 0
        while num > 0:
            digit_sum += num % 10
            num = num/10
        return digit_sum % 2 == 0

    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            count = 0
            for i in range(1, num+1):
                if i % 2 == 0:
                    count += 1
            return count

        total_count = total_count = 4 + (num-10)//10 * 5
        
        start = num//10 * 10
        for i in range(start, num+1):
            if self.digitSum(i):
                total_count += 1
                
        return total_count
        

    