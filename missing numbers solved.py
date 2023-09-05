def missingNumber(nums):
        y = sorted(nums)
        for i in range(len(y)+1):
            if i not in y:
                print(i) 


missingNumber(nums=[0,1])   

